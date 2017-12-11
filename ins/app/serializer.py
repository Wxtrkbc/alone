
import phonenumbers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from validate_email import validate_email

from ins.app.models import Ins, Tag, Comment

User = get_user_model()


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag


class UserSerializer(serializers.ModelSerializer):

    """
    uuid = UUIDField(read_only=True)
    password = CharField(max_length=128)
    last_login = DateTimeField(allow_null=True, required=False)
    created_at = DateTimeField(read_only=True)
    updated_at = DateTimeField(read_only=True)
    name = CharField(max_length=64, validators=[<UniqueValidator(queryset=User.objects.all())>])
    email = CharField(allow_blank=True, max_length=256, required=False)
    phone = CharField(allow_blank=True, max_length=16, required=False)
    avatar = CharField(allow_blank=True, max_length=256, required=False)
    location = CharField(allow_blank=True, required=False, style={'base_template': 'textarea.html'})
    sex = ChoiceField(choices=(('MALE', 'Male'), ('FEMALE', 'Female'), ('UNDEFINED', 'Undefined')), required=False)
    brief = CharField(allow_blank=True, max_length=512, required=False)
    level = ChoiceField(choices=(('NORMAL', 'Normal'), ('STAR', 'Star'), ('Superstar', 'Superstar')), required=False)

    """

    followers_count = serializers.IntegerField()
    following_count = serializers.IntegerField()

    class Meta:
        model = User
        exclude = ('is_admin', 'followed', 'updated_at', 'password')

    def validate_phone(self, value):
        try:
            res = phonenumbers.parse(value)
            if not phonenumbers.is_valid_number(res):
                raise serializers.ValidationError("Phone number seems not valid")
        except Exception as e:
            raise serializers.ValidationError("Phone number seems not valid")
        return value

    def validate_email(self, value):
        if not validate_email(value):
            raise serializers.ValidationError("Email seems not valid")
        return value

    def create(self, validated_data):
        # check_body_keys(validated_data, ['name', 'password'])
        name = validated_data.pop('name')
        password = validated_data.pop('password')
        return User.objects.create_user(username=name, password=password, **validated_data)

    def update(self, instance, validated_data):
        for key in ['location', 'avatar', 'location', 'sex', 'brief', 'email', 'phone']:
            if key in validated_data:
                setattr(instance, key, validated_data[key])
        instance.save()
        return instance


class UserSimpleSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'uuid': value.uuid,
            'name': value.name,
            'avatar': value.avatar
        }


class InsSerializer(serializers.ModelSerializer):
    owner = UserSimpleSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False)
    urls = serializers.JSONField(required=False)
    comments_count = serializers.IntegerField()
    likes_count = serializers.IntegerField()

    class Meta:
        model = Ins
        exclude = ('updated_at', 'likes')

    def create(self, validate_data):
        validate_data['owner'] = self.context['request'].user
        tags = validate_data.pop('tags', None)
        if tags:
            ret = []
            for item in tags:
                tag, _ = Tag.objects.get_or_create(name=item['name'])
                ret.append(tag)
        ins = Ins.objects.create(**validate_data)
        if ret:
            ins.tags.add(*ret)
        return ins


class CommentSerializer(serializers.ModelSerializer):
    poster = UserSimpleSerializer(read_only=True)
    ins = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment

    def create(self, validate_data):
        poster = self.context['request'].user
        ins_uuid = self.context['request'].parser_context['kwargs']['parent_lookup_uuid']
        ins = get_object_or_404(Ins, uuid=ins_uuid)
        content = validate_data.get('content')
        return Comment.objects.create(ins=ins, poster=poster, content=content)

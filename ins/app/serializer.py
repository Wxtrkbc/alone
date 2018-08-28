
import phonenumbers
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from validate_email import validate_email

from ins.app.models import Ins, Tag, Comment, Notification
from ins.utils.exception import AloneException
from ins.utils import errors

User = get_user_model()


class UserSimpleSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'uuid': value.uuid,
            'name': value.name,
            'avatar': value.avatar
        }


class InsSimpleSerializer(serializers.RelatedField):
    def to_representation(self, value):
        return {
            'uuid': value.uuid,
            'urls': value.urls
        }


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        # exclude = ('id', )


class UserSerializer(serializers.ModelSerializer):

    followers_count = serializers.IntegerField(required=False)
    following_count = serializers.IntegerField(required=False)
    post_count = serializers.IntegerField(required=False)
    relation = serializers.CharField(required=False)

    class Meta:
        model = User
        exclude = ('followed', 'updated_at')

    def to_representation(self, obj):
        rep = super(UserSerializer, self).to_representation(obj)
        rep.pop('password', None)
        return rep

    def validate_phone(self, value):
        res = phonenumbers.parse(value)
        if not phonenumbers.is_valid_number(res):
            raise serializers.ValidationError("Phone number seems not valid")
        if User.objects.filter(phone=value):
            raise AloneException(code=errors.ERR_PHONE_ALREADY_REGISTERED,
                                 message="The phone has been registered")
        return value

    def validate_email(self, value):
        if not validate_email(value):
            raise serializers.ValidationError("Email seems not valid")
        if User.objects.filter(email=value):
            raise AloneException(code=errors.ERR_EMAIL_ALREADY_REGISTERED,
                                 message="The email has been registered")
        return value

    def update(self, instance, validated_data):
        for key in ['location', 'avatar', 'location', 'sex', 'brief', 'email', 'phone']:
            if key in validated_data:
                setattr(instance, key, validated_data[key])
        instance.save()
        return instance


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


class InsSerializer(serializers.ModelSerializer):
    owner = UserSimpleSerializer(read_only=True)
    tags = TagSerializer(many=True, required=False)
    urls = serializers.JSONField(required=False)
    comments_count = serializers.IntegerField(required=False)
    likes_count = serializers.IntegerField(required=False)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Ins
        exclude = ('updated_at', 'likes')

    def create(self, validate_data):
        validate_data['owner'] = self.context['request'].user
        tags = validate_data.pop('tags', None)
        ret = []
        if tags:
            for item in tags:
                tag, _ = Tag.objects.get_or_create(name=item['name'])
                ret.append(tag)
        ins = Ins.objects.create(**validate_data)
        if ret:
            ins.tags.add(*ret)
        return ins


class NotifySerializer(serializers.ModelSerializer):

    sender = UserSimpleSerializer(read_only=True)
    ins = InsSimpleSerializer(read_only=True)

    class Meta:
        model = Notification


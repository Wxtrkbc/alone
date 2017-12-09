
import phonenumbers
from django.contrib.auth import get_user_model
from rest_framework import serializers
from validate_email import validate_email

from ins.app.models import Ins, Tag

User = get_user_model()


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

    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = ('is_admin', 'followed', 'updated_at')

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

    @staticmethod
    def get_followers(obj):
        return obj.followers.count()

    @staticmethod
    def get_following(obj):
        return obj.followed.count()


class InsSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(required=False, queryset=User.objects.all())
    tags = serializers.PrimaryKeyRelatedField(allow_empty=True, required=False,
                                              many=True, queryset=Tag.objects.all())

    class Meta:
        model = Ins

    def create(self, validate_data):
        user = self.context['request'].user
        brief = validate_data.get('brief', '')
        urls = validate_data.get('urls', [])
        return Ins.objects.create(brief=brief, urls=urls, owner=user)


from django.contrib.auth import get_user_model
from rest_framework import serializers

from alone.utils.func import check_body_keys

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    # password = serializers.CharField(write_only=True)

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

    class Meta:
        model = User
        exclude = ('is_admin', 'followed')

    def create(self, validated_data):
        # check_body_keys(validated_data, ['name', 'password'])
        name = validated_data.pop('name')
        password = validated_data.pop('password')
        return User.objects.create_user(username=name, password=password, **validated_data)


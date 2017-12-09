# coding=utf-8

URL_REGEX = '[A-Za-z0-9-_.]+'

# model file choice
SEX_MALE = "MALE"
SEX_FEMALE = 'FEMALE'
SEX_UNDEFINED = "UNDEFINED"

SEX_TYPES = (
    (SEX_MALE, 'Male'),
    (SEX_FEMALE, 'Female'),
    (SEX_UNDEFINED, 'Undefined')
)

USER_NORMAL = "NORMAL"
USER_STAR = "STAR"
USER_SUPERSTAR = "Superstar"

USER_LEVELS = (
    (USER_NORMAL, 'Normal'),
    (USER_STAR, 'Star'),
    (USER_SUPERSTAR, 'Superstar'),
)

PICTURE_INS = "PICTURE-INS"
VIDEO_INS = "VIDEO-INS"

INS_TYPE = (
    (PICTURE_INS, 'picture_ins'),
    (VIDEO_INS, 'video_ins')
)

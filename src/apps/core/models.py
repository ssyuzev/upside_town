import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now


def user_directory_path(instance, filename):
    """File will be upload to 'MEDIA_ROOT/user/<timestamp>/<filename>'."""
    timestamp = int(datetime.datetime.timestamp(now()))
    return f"users/{timestamp}/{filename}"


def validate_image(image):
    """Validate image file size."""
    file_size = image.file.size
    limit_mb = settings.UPLOAD_MAX_SIZE_MB
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


GENDERS = (
    ("m", "Male"),
    ("f", "Female"),
)


class Person(models.Model):

    photo = models.ImageField(upload_to=user_directory_path, validators=[validate_image])
    email = models.EmailField(unique=True, blank=False)
    gender = models.CharField(max_length=1, choices=GENDERS, default="m", blank=False)
    full_name = models.CharField(max_length=150, blank=False, default="")
    longitude = models.FloatField()
    latitude = models.FloatField()

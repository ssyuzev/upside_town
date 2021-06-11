import datetime

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.timezone import now

from PIL import Image, ImageOps


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

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    def save(self, *args, **kwargs):
        """Save new Person and flip the photo."""
        super(Person, self).save(*args, **kwargs)
        image = Image.open(self.photo.path)
        if image.width > 800 or image.height > 600:
            output_size = (800, 600)
            image.thumbnail(output_size)
        image = ImageOps.flip(image)
        image.save(self.photo.path)


class Like(models.Model):

    from_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="from_person")
    to_person = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name="to_person")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.from_person.full_name} to {self.to_person.full_name}"

    class Meta:
        unique_together = ('from_person', 'to_person',)

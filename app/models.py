from django.db import models
from django.utils.html import mark_safe


# Create your models here.
class Quote(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'


class UpcomingProjects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ManyToManyField('AppImage')

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="150" height="150">' % self.image.all().first().url)
    #
    # image_tag.short_description = 'Image'

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ManyToManyField('AppImage')
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

    # def image_tag(self):
    #     return mark_safe('<img src="%s" width="150" height="150">' % self.image.url)

    # image_tag.short_description = 'Image'

    def __str__(self):
        return f'{self.name} - {self.location}'


class Testimonial(models.Model):
    # name = models.CharField(max_length=100, blank=True, null=True)
    # occupation = models.CharField(max_length=100, blank=True, null=True)
    # testimony = models.TextField(blank=True, null=True)
    # rating = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)

    # def __str__(self):
    #     return f'{self.name} - {self.testimony}'


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        ordering = ['name']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'
        unique_together = (('name', 'email'),)


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='team_members/')

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150">' % self.image.url)

    image_tag.short_description = 'Image'

    def __str__(self):
        return f'{self.name} - {self.position}'


class AppImage(models.Model):
    imageLocation = 'images/'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imageLocation = kwargs.get('location')

    alt = models.TextField()
    image = models.ImageField(upload_to=imageLocation)

    def __str__(self):
        return f'{self.alt}'

class AssociatePartner(models.Model):
    image = models.ImageField(upload_to='associate_partners/')
from django.db import models


# Create your models here.
class Course(models.Model):
    img = models.ImageField(upload_to='course_images/')
    cname = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    lessons = models.CharField(max_length=50)
    enrolled = models.CharField(max_length=50)
    course_type=models.CharField(max_length=50)
    button_link = models.URLField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.cname
    
class Trainers(models.Model):
    imgt = models.ImageField(upload_to='teacher_images/')
    tname = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    facebook_link = models.URLField(blank=True,null=True)
    twitter_link = models.URLField(blank=True,null=True)
    linkedin_link = models.URLField(blank=True,null=True)
    instagram_link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.tname
    
class Enquire(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    msg=models.TextField()
    
class Testimonials(models.Model):
    imgts = models.ImageField(upload_to='teacher_images/')
    tsname = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.tsname
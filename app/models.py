from django.db import models
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class Plant(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(
        upload_to="plants/"
    )

    description = models.TextField(
        blank=True
    )

    page_name = models.CharField(max_length=100, default="")


    def __str__(self):
        return self.name



class MyPlant(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    plant = models.ForeignKey(
        Plant,
        on_delete=models.CASCADE
    )

    date_added = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.user.username + " - " + self.plant.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)

    def _str_(self):
        return self.user.username

class DiseaseInfo(models.Model):

    disease_name = models.CharField(
        max_length=200,
        unique=True
    )

    plant_name = models.CharField(
        max_length=100
    )

    symptoms = models.TextField()

    causes = models.TextField()

    treatment = models.TextField()

    prevention = models.TextField()


    def __str__(self):
        return self.disease_name



class ScanHistory(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    plant_name = models.CharField(max_length=100)

    disease_name = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to="scans/"
    )

    scanned_at = models.DateTimeField(
        auto_now_add=True
    )

    def _str_(self):
        return f"{self.user.username} - {self.disease_name}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create your models here.

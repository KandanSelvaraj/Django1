from django.db import models


# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=40)
    Email = models.CharField(max_length=40)
    password= models.CharField(max_length=12)
    confirmpassword= models.CharField(max_length=40)
    Address = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + " " + self.email + " " + self.password + " " + self.confirmpassword + " " + self.Address




    class Meta:
        ordering = ['created']

    class Meta:
        db_table = "blog_member"
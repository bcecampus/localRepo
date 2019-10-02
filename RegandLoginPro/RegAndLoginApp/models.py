from django.db import models

class Registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    batch=models.IntegerField()
    roll=models.CharField(max_length=10)

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    t1=models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    like=models.IntegerField()
    date=models.CharField(max_length=50)

class BranchInfo(models.Model):
    profile_photo=models.ImageField(upload_to='static/images')
    faculty_branch=models.CharField(max_length=50)
    faculty_name=models.CharField(max_length=100)
    faculty_description=models.CharField(max_length=100)

class CommentData(models.Model):
    feedback_id=models.IntegerField()
    comment_name=models.CharField(max_length=100)
    comment_text=models.CharField(max_length=500)
    comment_date=models.CharField(max_length=100)

class Like_Activity(models.Model):
    date_of_like=models.CharField(max_length=100)
    user_like=models.CharField(max_length=100)
    active=models.IntegerField()

class online(models.Model):
    Active_member=models.CharField(max_length=100)


from django.db import models
import re


class UserManager(models.Manager):
    def user_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['fname']) < 2:
            errors["fname"] = "** First name should be at least 2 characters **"
        if len(postData['lname']) < 2:
            errors["lname"] = "** Last name should be at least 2 characters **"
        for users in User.objects.filter(email = postData['email']):
            if users.email == postData['email']:
                errors["unique_email"] = "** Email has already been used, please login or try another **"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "** Invalid email address format **"
        if len(postData['password']) < 8:
            errors["password"] = "** Password should be at least 8 characters **"
        if postData['password'] != postData['checkPassword']:
            errors["checkPassword"] = "** Passwords must match **"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    #messages
    #comments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Message(models.Model):
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    message_text = models.TextField()
    #comments
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    comment_text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





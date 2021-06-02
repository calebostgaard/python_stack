from django.db import models
import re
from datetime import date, datetime, timedelta


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['inputFirstName']) < 2:
            errors["inputFirstName"] = "** First name should be at least 2 characters **"
        if len(postData['inputLastName']) < 2:
            errors["inputLastName"] = "** Last name should be at least 2 characters **"
        for users in User.objects.filter(email = postData['inputEmail']):
            if users.email == postData['inputEmail']:
                errors["show_unique_email"] = "** Email has already been used, please login or try another **"
        if not EMAIL_REGEX.match(postData['inputEmail']):
            errors['inputEmail'] = "** Invalid email address format **"
        if len(postData['inputPassword']) < 8:
            errors["inputPassword"] = "** Password should be at least 8 characters **"
        if postData['inputPassword'] != postData['checkPassword']:
            errors["checkPassword"] = "** Passwords must match **"
        
        today = date.today().isoformat()
        if postData['inputBirthday'] > today:
            errors["inputBirthday"] = "** Birth date must be in the past **"
                
        today = date.today()
        birthday = datetime.strptime(postData['inputBirthday'], "%Y-%m-%d").date()
        age = int((today - birthday).days / 365.2425)
        print(age)
        if age < 13:
            errors["inputTooYoung"] = "** You must be 13 years or older to register **"
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    birthday = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
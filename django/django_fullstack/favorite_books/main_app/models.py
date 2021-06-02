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
    # liked_books = a list of books a given user likes
    # books_uploaded = a list of books uploaded by a given user
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['book_title']) == 0:
            errors["book_title"] = "** Title is required **"
        if len(postData['book_desc']) < 5:
            errors["book_desc"] = "** Book description should be at least 5 characters **"
        for books in Book.objects.filter(title = postData['book_title']):
            if books.title == postData['book_title']:
                errors["unique_book"] = "** Book has already been added, please create a new book or add that book to favorites **"

        return errors


class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()


from django.db import models

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['show_title']) < 2:
            errors["show_title"] = "** Show title should be at least 2 characters **"
        for shows in Show.objects.filter(title = postData['show_title']):
            if shows.title == postData['show_title']:
                errors["show_unique_title"] = "** Show title has already been used, please try another **"
        if len(postData['show_network']) < 3:
            errors["dshow_networkesc"] = "** Show network should be at least 3 characters **"
        if len(postData['show_desc']) < 10:
            if len(postData['show_desc']) != 0:
                errors["show_desc"] = "** Show description should be at least 10 characters **"
        # if postData['show_release_date'] < *insert current date*
        #     errors["show_desc"] = "** Show date must be in the past **"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

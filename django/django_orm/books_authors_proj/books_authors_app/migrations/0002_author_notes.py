# Generated by Django 2.2.4 on 2021-01-15 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Nothing to say'),
            preserve_default=False,
        ),
    ]

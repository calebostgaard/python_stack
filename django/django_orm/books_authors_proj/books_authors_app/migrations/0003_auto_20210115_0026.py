# Generated by Django 2.2.4 on 2021-01-15 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_author_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Book'),
        ),
    ]

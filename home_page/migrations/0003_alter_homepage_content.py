# Generated by Django 4.2.11 on 2024-05-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0002_homepage_gamer_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='content',
            field=models.TextField(),
        ),
    ]
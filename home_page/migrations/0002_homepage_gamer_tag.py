# Generated by Django 4.2.11 on 2024-05-14 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='gamer_tag',
            field=models.ForeignKey(db_column='gamer_tag', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

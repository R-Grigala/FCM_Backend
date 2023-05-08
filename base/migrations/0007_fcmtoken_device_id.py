# Generated by Django 4.2 on 2023-05-08 12:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_fcmtoken_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='fcmtoken',
            name='device_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
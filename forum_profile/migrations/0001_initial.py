# Generated by Django 3.2 on 2023-12-16 07:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='profile/photo/%Y/%m/%d')),
                ('username', models.CharField(max_length=16)),
                ('description', models.TextField()),
                ('signature', models.TextField()),
                ('profile_color', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('username',),
            },
        ),
    ]

# Generated by Django 3.1.3 on 2020-12-08 21:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Python',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pythons')),
                ('wishes', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

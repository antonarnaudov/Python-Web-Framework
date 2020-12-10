# Generated by Django 3.1.3 on 2020-12-10 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pythons_app', '0003_auto_20201209_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='python',
            name='wishes',
        ),
        migrations.CreateModel(
            name='Wishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pythons_app.python')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
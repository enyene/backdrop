# Generated by Django 4.1.1 on 2022-09-07 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_photo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewedPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viewed_photo', to='core.photo')),
            ],
        ),
    ]
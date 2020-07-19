# Generated by Django 3.0.4 on 2020-07-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=75)),
                ('isbn', models.CharField(max_length=25)),
                ('review', models.TextField()),
                ('image', models.ImageField(upload_to='reviews/images/')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]

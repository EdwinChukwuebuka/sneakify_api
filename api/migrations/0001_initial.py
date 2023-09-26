# Generated by Django 4.2.1 on 2023-09-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sneaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
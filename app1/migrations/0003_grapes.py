# Generated by Django 3.1.1 on 2020-11-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_oranges'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grapes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name2', models.CharField(max_length=100)),
                ('price2', models.IntegerField()),
                ('desc2', models.TextField()),
                ('img2', models.ImageField(upload_to='pics')),
            ],
        ),
    ]

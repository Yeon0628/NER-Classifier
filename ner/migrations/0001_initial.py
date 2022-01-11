# Generated by Django 3.1.3 on 2021-12-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=25)),
                ('create_date', models.DateTimeField()),
                ('content', models.TextField()),
            ],
        ),
    ]
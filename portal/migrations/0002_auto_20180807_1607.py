# Generated by Django 2.1 on 2018-08-07 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_avatar', models.ImageField(height_field=50, upload_to='', width_field=50)),
                ('full_name', models.TextField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.TextField(max_length=10)),
                ('education_level', models.TextField(max_length=100)),
                ('field_of_study', models.TextField(max_length=100)),
                ('profession', models.TextField(max_length=10011111)),
                ('volunteer_type', models.TextField(max_length=50)),
                ('committee_type', models.TextField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
# Generated by Django 3.2.4 on 2021-07-26 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nid_no', models.CharField(max_length=17, unique=True)),
                ('name_bn', models.CharField(blank=True, max_length=100, null=True)),
                ('name_en', models.CharField(max_length=100)),
                ('father_name_bn', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_name_bn', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('village', models.CharField(blank=True, max_length=100, null=True)),
                ('road_no', models.CharField(blank=True, max_length=100, null=True)),
                ('post_name', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=8, null=True)),
            ],
        ),
    ]

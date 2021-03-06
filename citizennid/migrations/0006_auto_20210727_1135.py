# Generated by Django 3.2.4 on 2021-07-27 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citizennid', '0005_alter_citizennid_village'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citizennid',
            name='post_code',
        ),
        migrations.RemoveField(
            model_name='citizennid',
            name='post_name',
        ),
        migrations.AddField(
            model_name='village',
            name='post_code',
            field=models.CharField(blank=True, choices=[('3070', '3070')], default='3070', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='village',
            name='post_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='citizennid',
            name='road_no',
            field=models.CharField(blank=True, max_length=26, null=True),
        ),
        migrations.AlterField(
            model_name='village',
            name='word_no',
            field=models.CharField(blank=True, choices=[('1', '1 (Nurpur)'), ('2', '2 (Vujna)'), ('3', '3 (Sharifpur)'), ('4', '4 (Girishnagor)'), ('5', '5 (Tengratila)'), ('6', '6 (Tilagaon)'), ('7', '7 (Alipur)'), ('8', '8 (Mahobbatpur)'), ('9', '9 (Borkatnagor)')], max_length=2, null=True),
        ),
    ]

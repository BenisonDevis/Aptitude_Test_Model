# Generated by Django 4.2.1 on 2023-05-26 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_question_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='ans',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
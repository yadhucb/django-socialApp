# Generated by Django 4.0.3 on 2022-07-23 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='related_language',
            field=models.CharField(choices=[('Other', 'Other'), ('Python', 'Python'), ('Java', 'Java'), ('Ruby', 'Ruby'), ('HTML', 'HTML'), ('JavaScript', 'JavaScript'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('PHP', 'PHP'), ('SQL', 'SQL'), ('Swift', 'Swift')], max_length=12, null=True),
        ),
    ]

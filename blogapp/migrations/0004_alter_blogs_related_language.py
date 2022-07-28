# Generated by Django 4.0.3 on 2022-07-23 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_alter_blogs_related_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='related_language',
            field=models.CharField(blank=True, choices=[('Python', 'Python'), ('Java', 'Java'), ('Ruby', 'Ruby'), ('HTML', 'HTML'), ('JavaScript', 'JavaScript'), ('C', 'C'), ('C++', 'C++'), ('C#', 'C#'), ('PHP', 'PHP'), ('SQL', 'SQL'), ('Swift', 'Swift'), ('Other', 'Other')], max_length=12, null=True),
        ),
    ]
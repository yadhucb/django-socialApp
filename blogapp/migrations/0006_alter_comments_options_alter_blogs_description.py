# Generated by Django 4.0.3 on 2022-07-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_comments_options_comments_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-updated_at']},
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]

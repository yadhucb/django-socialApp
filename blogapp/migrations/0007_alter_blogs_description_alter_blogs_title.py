# Generated by Django 4.0.6 on 2022-07-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_alter_comments_options_alter_blogs_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(default='hoo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

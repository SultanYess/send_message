# Generated by Django 5.0 on 2023-12-07 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0005_alter_snippet_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]

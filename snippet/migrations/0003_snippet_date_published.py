# Generated by Django 5.0 on 2023-12-07 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0002_alter_snippet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
    ]

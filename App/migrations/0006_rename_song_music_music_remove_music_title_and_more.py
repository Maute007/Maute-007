# Generated by Django 4.2 on 2023-05-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_rename_tilte_music_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='song',
            new_name='music',
        ),
        migrations.RemoveField(
            model_name='music',
            name='title',
        ),
        migrations.AddField(
            model_name='music',
            name='title_music',
            field=models.CharField(default=1, max_length=80),
            preserve_default=False,
        ),
    ]

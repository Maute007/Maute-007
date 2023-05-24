# Generated by Django 4.2 on 2023-05-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_alter_music_title_music'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('home_title', models.CharField(max_length=50)),
                ('icon_title', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('card_title01', models.CharField(max_length=50)),
                ('color01', models.CharField(max_length=50)),
                ('card_icon01', models.CharField(max_length=50)),
                ('txt_card_a1', models.CharField(max_length=50)),
                ('txt_card_b1', models.CharField(max_length=50)),
                ('txt_card_c1', models.CharField(max_length=50)),
                ('card_title02', models.CharField(max_length=50)),
                ('color02', models.CharField(max_length=50)),
                ('card_icon02', models.CharField(max_length=50)),
                ('txt_card_a2', models.CharField(max_length=50)),
                ('txt_card_b2', models.CharField(max_length=50)),
                ('txt_card_c2', models.CharField(max_length=50)),
                ('btn_color', models.CharField(max_length=50)),
                ('icon_type', models.CharField(max_length=50)),
                ('Modal_title', models.CharField(max_length=50)),
                ('Modal_card_title', models.CharField(max_length=50)),
                ('modal_card_color', models.CharField(max_length=50)),
                ('modal_card_icon', models.CharField(max_length=50)),
                ('cargo01', models.CharField(max_length=50)),
                ('cargo02', models.CharField(max_length=50)),
                ('cargo03', models.CharField(max_length=50)),
                ('cargo04', models.CharField(max_length=50)),
                ('cargo05', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Pagina Principal',
            },
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-18 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_info.player')),
            ],
        ),
    ]

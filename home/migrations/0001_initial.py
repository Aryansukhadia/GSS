# Generated by Django 4.2.2 on 2023-07-31 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=122)),
                ('subject', models.CharField(max_length=122)),
                ('message', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(default='', max_length=30)),
                ('MATCHES_PLAYED', models.IntegerField(default=0)),
                ('MATCHES_WON', models.IntegerField(default=0)),
                ('MATCHES_DRAW', models.IntegerField(default=0)),
                ('TOTAL_GOALS_SCORED', models.IntegerField(default=0)),
                ('TOTAL_GOALS_AGAINST', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('te_name', models.CharField(max_length=40)),
                ('te_trophies', models.IntegerField()),
                ('team_home', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Upcomingmatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=40)),
                ('team2', models.CharField(max_length=40)),
                ('ma_venue', models.CharField(default='', max_length=40)),
                ('ma_date', models.DateField()),
                ('ma_time', models.TimeField()),
                ('ma_desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Addplayers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players_type', models.CharField(choices=[('one', 'chaser'), ('two', 'keeper'), ('three', 'beaters'), ('four', 'seeker')], default='', max_length=15)),
                ('player_name', models.CharField(max_length=30)),
                ('team', models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.teams')),
            ],
        ),
    ]

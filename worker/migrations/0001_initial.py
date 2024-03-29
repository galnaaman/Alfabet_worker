# Generated by Django 4.2.9 on 2024-02-03 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('location', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('popularity', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'events',
                'ordering': ['id'],
                'managed': False,
            },
        ),
    ]

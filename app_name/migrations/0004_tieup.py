# Generated by Django 4.2.2 on 2023-07-13 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0003_blog_contact_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tieup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.TextField()),
            ],
            options={
                'db_table': 'tieup',
            },
        ),
    ]
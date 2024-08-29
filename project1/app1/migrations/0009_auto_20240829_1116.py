# Generated by Django 3.2.19 on 2024-08-29 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_alter_posts_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]

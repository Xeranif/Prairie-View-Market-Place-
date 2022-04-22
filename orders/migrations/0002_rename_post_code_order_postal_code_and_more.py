# Generated by Django 4.0.3 on 2022-04-22 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='post_code',
            new_name='postal_code',
        ),
        migrations.AddField(
            model_name='order',
            name='country_code',
            field=models.CharField(blank=True, max_length=4),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_option',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 5.1.6 on 2025-02-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='membership_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='membership_type',
            field=models.CharField(blank=True, choices=[('Silver', 'Silver'), ('Gold', 'Gold'), ('Diamond', 'Diamond')], max_length=10, null=True),
        ),
    ]

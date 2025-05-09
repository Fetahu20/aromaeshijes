# Generated by Django 5.2 on 2025-05-09 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0007_alter_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_subject', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_message', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

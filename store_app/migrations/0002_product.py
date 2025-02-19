# Generated by Django 5.1.6 on 2025-02-17 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('article', models.CharField(db_index=True, help_text='Unique string product id', max_length=100, unique=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store_app.category')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='store_app.supplier')),
            ],
        ),
    ]

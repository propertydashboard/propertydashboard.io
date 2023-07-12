# Generated by Django 4.2.3 on 2023-07-10 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('value', models.IntegerField(default=0)),
                ('mortgage', models.IntegerField(default=0)),
                ('current_rent', models.IntegerField(default=0)),
                ('market_rent', models.IntegerField(default=0)),
                ('photo', models.ImageField(default='', upload_to='images/')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'properties',
            },
        ),
    ]
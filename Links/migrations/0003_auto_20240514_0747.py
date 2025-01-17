# Generated by Django 3.1.3 on 2024-05-14 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Links', '0002_auto_20240514_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True)),
                ('tipo', models.TextField(blank=True)),
                ('nivel', models.TextField(blank=True)),
                ('color', models.TextField(blank=True)),
                ('image', models.URLField()),
                ('posted_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Links',
        ),
    ]

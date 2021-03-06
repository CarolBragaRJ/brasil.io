# Generated by Django 3.1.1 on 2020-10-02 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="auth_tokens",
                to=settings.AUTH_USER_MODEL,
                verbose_name="User",
            ),
        ),
    ]

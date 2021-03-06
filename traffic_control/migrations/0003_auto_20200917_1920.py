# Generated by Django 3.1.1 on 2020-09-17 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traffic_control", "0002_auto_20200917_1831"),
    ]

    operations = [
        migrations.AddField(model_name="blockedrequest", name="headers", field=models.JSONField(default=dict),),
        migrations.AddField(model_name="blockedrequest", name="path", field=models.TextField(default=""),),
        migrations.AddField(model_name="blockedrequest", name="query_string", field=models.JSONField(default=dict),),
        migrations.AddField(
            model_name="blockedrequest", name="source_ip", field=models.GenericIPAddressField(null=True),
        ),
        migrations.AddField(model_name="blockedrequest", name="user_agent", field=models.TextField(default=""),),
    ]

# Generated by Django 3.0.5 on 2020-07-06 21:05
from django.conf import settings
from django.db import migrations


def create_covid19_admin_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    group = Group.objects.create(name=settings.COVID_19_ADMIN_GROUP_NAME)

    states_perms = Permission.objects.filter(codename__startswith=settings.COVID_IMPORT_PERMISSION_PREFIX)
    group.permissions.add(*states_perms)

    perm_codes = ["add_statespreadsheet", "view_statespreadsheet"]
    group_permissions = Permission.objects.filter(codename__in=perm_codes)
    group.permissions.add(*group_permissions)


def delete_covid19_admin_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Group.objects.filter(name=settings.COVID_19_ADMIN_GROUP_NAME).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("covid19", "0010_auto_20200706_1504"),
    ]

    operations = [migrations.RunPython(create_covid19_admin_group, delete_covid19_admin_group)]

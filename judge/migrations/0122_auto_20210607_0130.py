# Generated by Django 2.2.23 on 2021-06-07 01:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('judge', '0121_merge_20210607_0120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contestproblem',
            options={'ordering': ('order',), 'verbose_name': 'contest problem', 'verbose_name_plural': 'contest problems'},
        ),
        migrations.AlterModelOptions(
            name='webauthncredential',
            options={'verbose_name': 'WebAuthn credential', 'verbose_name_plural': 'WebAuthn credentials'},
        ),
    ]

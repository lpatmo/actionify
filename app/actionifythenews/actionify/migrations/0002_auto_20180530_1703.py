# Generated by Django 2.0.5 on 2018-05-30 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actionify', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventaction',
            unique_together={('eventID', 'actionID')},
        ),
        migrations.AlterUniqueTogether(
            name='eventtag',
            unique_together={('eventID', 'tagID')},
        ),
        migrations.AlterUniqueTogether(
            name='spamaction',
            unique_together={('actionID', 'userID')},
        ),
        migrations.AlterUniqueTogether(
            name='uservote',
            unique_together={('userID', 'actionID')},
        ),
        migrations.AlterUniqueTogether(
            name='watchedevent',
            unique_together={('userID', 'eventID')},
        ),
    ]

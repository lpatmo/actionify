# Generated by Django 2.0.5 on 2018-05-30 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionType', models.CharField(choices=[('petition', 'Petition'), ('donation', 'Donation'), ('vote', 'Vote'), ('call', 'Call'), ('attend_an_event', 'Attend an Event'), ('other', 'Other')], default='petition', max_length=20)),
                ('actionURL', models.CharField(max_length=1000)),
                ('votes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Action')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Event')),
            ],
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Event')),
            ],
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.CharField(max_length=1000)),
                ('eventID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actionify.Event')),
            ],
        ),
        migrations.CreateModel(
            name='SpamAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Action')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Default Tag', max_length=250)),
                ('event', models.ManyToManyField(to='actionify.Event')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvote', models.BooleanField()),
                ('actionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Action')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.User')),
            ],
        ),
        migrations.CreateModel(
            name='WatchedEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Event')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.User')),
            ],
        ),
        migrations.AddField(
            model_name='spamaction',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.User'),
        ),
        migrations.AddField(
            model_name='eventtag',
            name='tagID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Tag'),
        ),
        migrations.AddField(
            model_name='admin',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.User'),
        ),
        migrations.AddField(
            model_name='action',
            name='creatorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='actionify.User'),
        ),
    ]

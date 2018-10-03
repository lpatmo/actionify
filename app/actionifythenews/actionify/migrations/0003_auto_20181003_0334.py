# Generated by Django 2.0.5 on 2018-10-03 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actionify', '0002_auto_20180530_1703'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.Action')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='useraction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actionify.User'),
        ),
        migrations.AlterUniqueTogether(
            name='useraction',
            unique_together={('user', 'actionID')},
        ),
    ]

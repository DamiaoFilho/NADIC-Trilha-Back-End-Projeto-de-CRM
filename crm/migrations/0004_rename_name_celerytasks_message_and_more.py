# Generated by Django 4.1.7 on 2023-07-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_celerytasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='celerytasks',
            old_name='name',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='celerytasks',
            name='file',
        ),
        migrations.RemoveField(
            model_name='celerytasks',
            name='status',
        ),
        migrations.AddField(
            model_name='celerytasks',
            name='response',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-22 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_application_modeofinterview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='inPersonVisitTime',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='interviewTime',
            field=models.TimeField(default=''),
        ),
        migrations.AlterField(
            model_name='application',
            name='modeOfInterview',
            field=models.CharField(choices=[('Online Interview', 'Online Interview'), ('On-site Interview', 'On-site Interview')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='preferredModeOfInterview',
            field=models.CharField(choices=[('Online Interview', 'Online Interview'), ('On-site Interview', 'On-site Interview')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Interviewing', 'Interviewing'), ('Accepted', 'Accepted'), ('On Hold', 'On Hold'), ('Rejected', 'Rejected'), ('Evaluating', 'Evaluating'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
    ]

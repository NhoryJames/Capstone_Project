# Generated by Django 4.2.7 on 2023-11-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('On Hold', 'On Hold'), ('Rejected', 'Rejected')], max_length=50),
        ),
        migrations.AlterField(
            model_name='condoagreement',
            name='condoAgreement',
            field=models.FileField(blank=True, null=True, upload_to='static/application_files'),
        ),
    ]
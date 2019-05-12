# Generated by Django 2.1.7 on 2019-05-12 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miniproject', '0004_auto_20190512_0807'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Qsubject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='miniproject.Subject'),
        ),
        migrations.AlterField(
            model_name='question',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='miniproject.Professor'),
        ),
    ]
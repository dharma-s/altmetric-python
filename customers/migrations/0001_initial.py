# Generated by Django 5.0.4 on 2024-04-09 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Platinum365', 'Platinum365'), ('Gold180', 'Gold180'), ('Silver90', 'Silver90')], max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('validity', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
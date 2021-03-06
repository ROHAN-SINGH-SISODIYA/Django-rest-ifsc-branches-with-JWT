# Generated by Django 2.2.3 on 2019-07-06 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=500, unique=True)),
                ('name', models.CharField(max_length=256)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=500)),
                ('district', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Bank')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branch',
                'ordering': ('name',),
            },
        ),
    ]

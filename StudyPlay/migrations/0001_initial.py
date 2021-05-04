# Generated by Django 2.1.15 on 2021-05-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=100)),
                ('Subject', models.CharField(db_column='Subject', max_length=100)),
            ],
            options={
                'db_table': 'activities',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='AdminModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('Adminid', models.CharField(db_column='Adminid', max_length=9)),
                ('Pseudo', models.CharField(db_column='Pseudo', max_length=10)),
                ('Password', models.CharField(db_column='Password', max_length=10)),
                ('Email', models.TextField(db_column='Email')),
            ],
            options={
                'db_table': 'admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ChildModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('Pseudo', models.CharField(db_column='Pseudo', max_length=10)),
                ('Password', models.CharField(db_column='Password', max_length=100)),
                ('Age', models.TextField(db_column='Age')),
                ('Email', models.TextField(db_column='Email')),
                ('ParentsPseudo', models.CharField(db_column='ParentsPseudo', max_length=100)),
            ],
            options={
                'db_table': 'child',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CountriesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(db_column='Name', max_length=100)),
                ('Count', models.IntegerField(db_column='Count', default=0)),
            ],
            options={
                'db_table': 'countries',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ParentsModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('Pseudo', models.CharField(db_column='Pseudo', max_length=10)),
                ('Password', models.CharField(db_column='Password', max_length=100)),
                ('Email', models.TextField(db_column='Email')),
                ('country', models.TextField(db_column='country')),
            ],
            options={
                'db_table': 'Parents',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WorkersModel',
            fields=[
                ('ID', models.IntegerField(db_column='ID', primary_key=True, serialize=False)),
                ('Workerid', models.CharField(db_column='Workerid', max_length=10)),
                ('Pseudo', models.CharField(db_column='Pseudo', max_length=10)),
                ('Password', models.CharField(db_column='Password', max_length=4)),
                ('Email', models.TextField(db_column='Email')),
                ('type', models.TextField(db_column='type')),
            ],
            options={
                'db_table': 'workers',
                'managed': True,
            },
        ),
    ]

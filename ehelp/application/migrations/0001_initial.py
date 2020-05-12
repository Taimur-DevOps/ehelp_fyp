# Generated by Django 3.0.2 on 2020-05-11 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('image_height', models.PositiveIntegerField(blank=True, default='150', editable=False, null=True)),
                ('image_width', models.PositiveIntegerField(blank=True, default='150', editable=False, null=True)),
                ('full_name', models.CharField(max_length=255)),
                ('profile', models.ImageField(default='images/profiles/user-blank-image.png', height_field='image_height', help_text='Profile Picture', upload_to='images/profiles/', verbose_name='Profile Picture', width_field='image_width')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True)),
                ('facebook', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('points', models.IntegerField(blank=True, default=0, null=True)),
                ('requests', models.IntegerField(blank=True, default=0, null=True)),
                ('responses', models.IntegerField(blank=True, default=0, null=True)),
                ('hearts', models.IntegerField(blank=True, default=0, null=True)),
                ('subscribers', models.IntegerField(blank=True, default=0, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('currency', models.CharField(blank=True, max_length=50, null=True)),
                ('lang', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('supply', models.BooleanField(default=0)),
                ('delivered', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='application.Country')),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
        ),
        migrations.CreateModel(
            name='Request_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Request Categories',
            },
        ),
        migrations.CreateModel(
            name='Request_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Request Status',
            },
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField(blank=True, null=True)),
                ('request_points', models.IntegerField(blank=True, default=0, null=True)),
                ('shipment_points', models.IntegerField(blank=True, default=0, null=True)),
                ('other_points', models.IntegerField(blank=True, default=0, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Request')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Responses',
            },
        ),
        migrations.CreateModel(
            name='Request_Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/requests/')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Request')),
            ],
            options={
                'verbose_name_plural': 'Cities',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='request_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='application.Request_Category'),
        ),
        migrations.AddField(
            model_name='request',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Request')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Queues',
            },
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.Country'),
        ),
        migrations.AddField(
            model_name='account',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.City'),
        ),
        migrations.AddField(
            model_name='account',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Country'),
        ),
    ]
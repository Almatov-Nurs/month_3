# Generated by Django 4.0.1 on 2022-01-31 12:18

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'ADMIN'), (2, 'VIP-Client'), (3, 'CLIENT')], default=3, verbose_name='тип пользователя')),
                ('phone_number', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE')])),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

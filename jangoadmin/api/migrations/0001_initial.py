# Generated by Django 3.0.14 on 2021-04-12 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('latitude', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Latitude')),
                ('longitude', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Latitude')),
                ('my_description', models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='Latitude')),
                ('twitter_handle', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Twitter Handle')),
                ('facebook_handle', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Facebook Handle')),
                ('instagram_token', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Instagram Handle')),
                ('paypal_email', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Paypal email')),
                ('device_token', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Device Token')),
                ('onetime_token', models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='OneTime token')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created On')),
                ('updated_on', models.DateTimeField(auto_now_add=True, verbose_name='Updated On')),
                ('email', models.EmailField(error_messages={'unique': 'OOPS,An account with this email is already regisgtered'}, max_length=254, unique=True, verbose_name='Email')),
                ('username', models.CharField(error_messages={'unique': 'An UserName with this username is already regisgtered'}, max_length=100, unique=True, verbose_name='UserName')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

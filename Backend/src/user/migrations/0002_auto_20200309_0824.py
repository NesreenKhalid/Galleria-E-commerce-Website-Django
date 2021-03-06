# Generated by Django 3.0.3 on 2020-03-09 08:24

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200309_0803'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100, verbose_name='User Name')),
                ('user_password', models.CharField(max_length=128, verbose_name='User Password')),
                ('user_email', models.EmailField(blank=True, default='', max_length=254, unique=True, verbose_name='Email')),
                ('user_phone', models.CharField(max_length=128, verbose_name='User Phone')),
                ('user_pic', models.ImageField(upload_to='user/', verbose_name='Profile Picture')),
                ('user_credit_id', models.CharField(max_length=128, verbose_name='Credit Card ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Last Login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='product ID')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='product ID')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='product ID')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='UID',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='user ID'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.3 on 2023-01-09 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('1_in_cart', 'in_cart'), ('2_waiting_for_payment', 'waiting_for_payment'), ('3_paid', 'paid')], default='1_in_cart', max_length=32)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='product_name')),
                ('code', models.CharField(max_length=255, verbose_name='product_code')),
                ('price', models.DecimalField(decimal_places=2, max_digits=28)),
                ('unit', models.CharField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrederItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.PositiveIntegerField(default=1)),
                ('prices', models.DecimalField(decimal_places=2, max_digits=20)),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='store.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

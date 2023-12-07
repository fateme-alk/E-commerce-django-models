# Generated by Django 4.2.7 on 2023-12-07 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.PositiveBigIntegerField()),
                ('payment_method', models.CharField(choices=[('Digital wallets', 'Digital wallets'), ('Cash', 'Cash'), ('Gift card', 'Gift card'), ('Credit card', 'Credit card')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('treansaction_num', models.PositiveBigIntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='ordered_products',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.PositiveBigIntegerField()),
                ('products', models.ManyToManyField(to='products.product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.transaction')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(to='products.order'),
        ),
    ]

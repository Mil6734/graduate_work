# Generated by Django 4.2.5 on 2023-10-26 19:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('courier', 'Наличными курьеру'), ('card_courier', 'Картой курьеру'), ('card_online', 'Картой онлайн')], max_length=20, verbose_name='Способ оплаты')),
                ('created_data', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('CREATED', 'Создан'), ('PAI', 'Оплачен'), ('DELIVERED', 'Доставлен в службу доставки')], default='CREATED', max_length=20, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=200, verbose_name='Почта')),
                ('phone', models.CharField(max_length=200, verbose_name='Телефон')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('zipcode', models.CharField(max_length=200, verbose_name='Зип код')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
            ],
            options={
                'verbose_name': 'заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='Количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар в заказе',
                'verbose_name_plural': 'Товары в заказе',
            },
        ),
    ]

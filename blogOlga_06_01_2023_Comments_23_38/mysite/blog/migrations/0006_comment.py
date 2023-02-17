# Generated by Django 4.1.2 on 2023-01-01 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный адрес')),
                ('body', models.TextField(verbose_name='Содержание комментария')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('active', models.BooleanField(default=False, verbose_name='Активный')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post', verbose_name='Отношение к статъе')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created_on'],
            },
        ),
    ]
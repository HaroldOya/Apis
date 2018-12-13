# Generated by Django 2.0.9 on 2018-12-13 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ofertasBlog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('precio', models.CharField(max_length=20)),
                ('producto', models.CharField(max_length=300)),
                ('imagen', models.CharField(max_length=200)),
                ('oferta', models.CharField(max_length=20)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='perro',
            name='author',
        ),
        migrations.DeleteModel(
            name='Perro',
        ),
    ]
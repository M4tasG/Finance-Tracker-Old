# Generated by Django 3.1.6 on 2021-03-20 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='ttype',
            new_name='transaction_class',
        ),
        migrations.AddField(
            model_name='classification',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='transaction',
            name='balance',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.balance'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(blank=True, default='Spending', max_length=12),
        ),
    ]

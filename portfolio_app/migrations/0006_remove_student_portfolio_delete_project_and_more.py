# Generated by Django 5.0.2 on 2024-02-27 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_remove_portfolio_student_student_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='portfolio',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
    ]
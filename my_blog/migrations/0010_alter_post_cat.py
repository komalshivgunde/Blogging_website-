# Generated by Django 4.2.6 on 2023-11-07 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0009_alter_category_cat_id_alter_post_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cat',
            field=models.ForeignKey(db_column='cid', on_delete=django.db.models.deletion.CASCADE, to='my_blog.category'),
        ),
    ]

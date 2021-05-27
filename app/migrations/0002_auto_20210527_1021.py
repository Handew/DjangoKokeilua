# Generated by Django 3.2.3 on 2021-05-27 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['productname']},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'ordering': ['companyname']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='packageSize',
            new_name='packagesize',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='productName',
            new_name='productname',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unitPrice',
            new_name='unitprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='unitsInStock',
            new_name='unitsinstock',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='companyName',
            new_name='companyname',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='contactName',
            new_name='contactname',
        ),
    ]
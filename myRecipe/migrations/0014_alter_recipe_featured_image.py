# Generated by Django 4.0.3 on 2022-05-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myRecipe', '0013_alter_recipe_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='featured_image',
            field=models.ImageField(blank=True, default='images/images/default.jpg', null=True, upload_to='images/userupload'),
        ),
    ]

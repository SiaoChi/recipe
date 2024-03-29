# Generated by Django 4.0.3 on 2022-03-09 16:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('detail', models.TextField(blank=True, null=True)),
                ('source_link', models.URLField(blank=True, max_length=2000, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sauce',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('detail', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myRecipe.recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(blank=True, to='myRecipe.tag'),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('unit', models.CharField(blank=True, max_length=20)),
                ('detail', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myRecipe.recipe')),
            ],
        ),
    ]

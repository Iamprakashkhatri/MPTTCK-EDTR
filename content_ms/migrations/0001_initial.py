# Generated by Django 2.1 on 2020-09-02 07:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('create_page', models.BooleanField()),
                ('show_in_menu', models.BooleanField()),
                ('active', models.CharField(choices=[('AC', 'ACTIVE'), ('PA', 'PASSIVE')], default='AC', max_length=100)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='content_ms.Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

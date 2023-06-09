# Generated by Django 4.1.7 on 2023-03-26 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='auther',
            new_name='author',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='book_image',
        ),
        migrations.RemoveField(
            model_name='bookmodel',
            name='contents',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='book_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='description',
            field=models.TextField(null=True),
        ),
    ]

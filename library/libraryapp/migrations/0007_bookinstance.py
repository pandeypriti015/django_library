# Generated by Django 2.2.6 on 2019-10-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0006_book_book_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete='on_delete=models.CASECADE', to='libraryapp.Book')),
            ],
        ),
    ]

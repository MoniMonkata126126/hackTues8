# Generated by Django 4.0.3 on 2022-03-12 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_alter_answer_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='result',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizes'},
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Result',
        ),
    ]

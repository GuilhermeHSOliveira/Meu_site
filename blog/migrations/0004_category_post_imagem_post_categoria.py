# Generated by Django 4.0.3 on 2022-03-22 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options_alter_post_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('published', models.DateField(default=django.utils.timezone.now)),
                ('create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ManyToManyField(related_name='get_posts', to='blog.category'),
        ),
    ]

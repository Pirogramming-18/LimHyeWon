# Generated by Django 4.1.5 on 2023-01-18 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devtool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('kind', models.CharField(max_length=30)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, upload_to='posts/%Y%m%d')),
                ('content', models.TextField()),
                ('interest', models.IntegerField()),
                ('devtool', models.CharField(choices=[('django', 'django'), ('react', 'react'), ('Spring', 'Spring'), ('Node.js', 'Node.js'), ('java', 'java'), ('c++', 'c++')], max_length=20, null=True)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='used_tool', to='posts.devtool')),
            ],
        ),
    ]
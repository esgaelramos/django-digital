# Generated by Django 4.0.3 on 2022-03-31 21:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import education.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.CharField(default='GR-ORG', max_length=7, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=education.models.topic_directory_path)),
                ('slug', models.SlugField(max_length=250, unique=True, unique_for_date='start')),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_complete', models.BooleanField(default=False)),
                ('humans', models.ManyToManyField(to='education.human')),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.subject')),
            ],
            options={
                'ordering': ('-start',),
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('lesson_number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('subtitle', models.CharField(max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to=education.models.lesson_directory_path)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out of Education', 'Out of Education'), ('Completed', 'Completed')], max_length=20, null=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.subject')),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.topic')),
            ],
            options={
                'ordering': ('-lesson_number',),
            },
        ),
        migrations.AddField(
            model_name='human',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='education.organization'),
        ),
    ]

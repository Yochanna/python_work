from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('title', models.CharField(max_length=200)),
                    ('blurb', models.TextField(blank=True)),
                    ('repo_url', models.URLField(blank=True)),
                    ('demo_url', models.URLField(blank=True)),
                    ('status', models.CharField(choices=[('draft','Draft'),('in_progress','In Progress'),('published','Published'),('archived','Archived')], default='draft', max_length=20)),
                    ('date_added', models.DateTimeField(auto_now_add=True))],
            options={'ordering':['-date_added']},
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                    ('image_url', models.URLField(blank=True)),
                    ('caption', models.CharField(blank=True, max_length=200)),
                    ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='projects.project'))],
        ),
    ]
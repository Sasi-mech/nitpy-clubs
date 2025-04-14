from django.db import migrations, models
import django.db.models.deletion

def add_default_club(apps, schema_editor):
    Club = apps.get_model('info', 'Club')
    ClubImage = apps.get_model('info', 'ClubImage')
    # Create a default club if none exists
    default_club, created = Club.objects.get_or_create(
        name='Default Club',
        defaults={'description': 'Default club description', 'logo': ''}
    )
    # Assign the default club to all existing ClubImage instances
    ClubImage.objects.update(club=default_club)

class Migration(migrations.Migration):
    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubimage',
            name='club',
            field=models.ForeignKey(
                null=True,  # Allow null temporarily
                on_delete=django.db.models.deletion.CASCADE,
                related_name='club_images',
                to='info.club'
            ),
        ),
        migrations.RunPython(add_default_club),
        migrations.AlterField(
            model_name='clubimage',
            name='club',
            field=models.ForeignKey(
                null=False,  # Disallow null after data migration
                on_delete=django.db.models.deletion.CASCADE,
                related_name='club_images',
                to='info.club'
            ),
        ),
        migrations.AlterField(
            model_name='club',
            name='gallery',
            field=models.ManyToManyField(blank=True, related_name='club_gallery', to='info.clubimage'),
        ),
    ]
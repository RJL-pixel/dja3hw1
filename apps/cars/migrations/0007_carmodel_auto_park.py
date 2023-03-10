from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_parks', '0001_initial'),
        ('cars', '0006_alter_carmodel_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_parks.autoparkmodel'),
            preserve_default=False,
        ),
    ]
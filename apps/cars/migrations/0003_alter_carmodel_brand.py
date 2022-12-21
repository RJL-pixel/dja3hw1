from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_carmodel_created_at_carmodel_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
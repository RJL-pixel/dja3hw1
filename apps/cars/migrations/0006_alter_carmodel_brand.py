import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_carmodel_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(20)]),
        ),
    ]
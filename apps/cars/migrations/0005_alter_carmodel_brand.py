import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_carmodel_body_alter_carmodel_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'Error two chars'), django.core.validators.MaxLengthValidator(20)]),
        ),
    ]
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('logo_image', models.ImageField(upload_to='uploads/coins')),
                ('price', models.FloatField()),
                ('details', models.TextField()),
            ],
        ),
    ]

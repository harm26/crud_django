from django.db import models

# Create your models here.

PARENTESCO=(
    ('mama', 'mama'),
    ('papa', 'papa'),
    ('hno', 'hermano'),
    ('hna', 'hermana'),
    ('esposa', 'esposa'),
    ('esposo', 'esposo'),
    ('hijo', 'hijo'),
    ('hija', 'hija'),

)
VIVE=(
    ('si','si'),
    ('no','no'),
)



class Familiares(models.Model):
    nombre= models.CharField(max_length=50)
    parentesco= models.CharField(max_length=50)
    vive= models.CharField(max_length=2)
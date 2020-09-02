from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField

class Genre(MPTTModel):
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50, unique=True)
    description = RichTextField(null=True,blank=True)
    create_page=models.BooleanField()
    show_in_menu=models.BooleanField()
    ACTIVE = "AC"
    PASSIVE = "PA"
    IS_ACTIVE = [
        (ACTIVE, 'ACTIVE'),
        (PASSIVE, 'PASSIVE'),
    ]
    active = models.CharField(
        max_length=100,
        choices=IS_ACTIVE,
        default=ACTIVE,
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name



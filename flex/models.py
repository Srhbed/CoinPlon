from django.db import models
from wagtail.core.models import Page 
from wagtail.admin.edit_handlers import FieldPanel


# Create your models here.
class FlexPage(Page):
    
    texte = models.TextField(
    
        blank=True,
        max_length=500
    )
      
    content_panels = Page.content_panels + [
        FieldPanel("texte")]
    
class Meta :
        verbose_name = "Page divers"
        verbose_name_plural = "Pages divers"

from unittest.util import _MAX_LENGTH
from django.db import models

from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel ,  PageChooserPanel , StreamFieldPanel
from streams import blocks
from wagtail.core.fields import StreamField

class HomePage(Page):
    lead_text=models.CharField(
        max_length=140,
        blank=True,
        help_text="sous-titre sous la banniére"
    )
    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text="Sélectionner une page à linker",
        on_delete=models.SET_NULL
    )
    button_text=models.CharField(
        max_length=50,
        default="Read More",
        blank=False,
        help_text="bouton pour le texte",
    )
    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        related_name="+",
        help_text="banniére arriére plan",
        on_delete = models.SET_NULL
        
    )
    
    body = StreamField([("title", blocks.TittleBlock())], null=True , blank=True )
       
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        FieldPanel("banner_background_image"),
        StreamFieldPanel("body")
        
    ]

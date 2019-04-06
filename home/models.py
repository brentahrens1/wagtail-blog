from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

class HomePage(Page):
    call_to_action = models.CharField(
        max_length = 255,
        blank = True,
        null = True
    )
    description = RichTextField(
        blank = True,
        null = True
    )
    content_panels = Page.content_panels + [
        FieldPanel('call_to_action'),
        FieldPanel('description')
    ]

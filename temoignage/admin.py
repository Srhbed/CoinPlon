from wagtail.contrib.modeladmin.options import ModelAdmin ,modeladmin_register

from .models import Temoignage




# Register your models here.
@modeladmin_register
class TemoignageAdmin(ModelAdmin):
    
    model = Temoignage
    menu_label =  "Temoignage"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    
 
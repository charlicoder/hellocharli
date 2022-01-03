from django.contrib import admin

# Register your models here.
from citizennid.models import CitizenNid, Village

class CitizenNidAdmin(admin.ModelAdmin):
    list_display = ['id', 'nid_no', 'name_en', 'birth_date', 'village']
    search_fields = ['nid_no', 'name_en']
    list_filter = ('gender','birth_date', 'village')


class VillageAdmin(admin.ModelAdmin):
    # fields = [('village_name', 'village_id'), ('post_name', 'post_code')]
    fieldsets = (
        ('Section 1', {
                'fields': ('village_name',)
        }),
        (' Geo code section', {
            'fields': (('village_id', 'village_code_old'),)
        }),
        ('Post codes', {
            'fields': (('post_code', 'post_name'),)
        })
    )

    # list_display = ['village_name', 'word_no', 'post_code']
    # search_fields = ['village_name', 'word_no']
    # list_filter = ('word_no', )

admin.site.register(CitizenNid, CitizenNidAdmin)

admin.site.register(Village, VillageAdmin)

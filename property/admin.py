from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnersInline(admin.TabularInline):
    model = Owner.owned_flats.through
    raw_id_fields = ('owner', )
    verbose_name = 'Владелец квартиры'
    verbose_name_plural = 'Владельцы квартиры'


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ('created_at',)
    list_display = (
                    'address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
    )
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony', 'floor')
    raw_id_fields = ('liked_by',)

    inlines = [OwnersInline]


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('owned_flats',)
    search_fields = ('owner',)


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

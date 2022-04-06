from django.contrib import admin
from baskets.models import Baskets


class BasketAdminInline(admin.TabularInline):
    model = Baskets
    fields = ('product', 'quantity', 'created_timestamp',)
    readonly_fields = ('quantity', 'created_timestamp',)
    extra = 0

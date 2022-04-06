from django.contrib import admin
from orders.models import Order, OrderItem
from django.utils.translation import ugettext as _


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'is_active', 'total_cost')
    inlines = (OrderItemInline,)
    readonly_fields = ('total_cost',)

    def get_total_cost(self, object):
        return object.total_cost

    get_total_cost.description = _('сумма заказа')

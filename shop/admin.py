from django.contrib import admin

# Register your models here.
from shop.models import Products, SubCategory, Category, Tags
from users.models import UserLeads


class ProductsAdmin(admin.ModelAdmin):
    model = Products
    readonly_fields = ('product_id',)


class UserLeadsAdmin(admin.ModelAdmin):
    model = UserLeads
    list_display = ( 'id', 'email', 'parent_company', 'utm_source', 'utm_medium', 'utm_campaign', 'child_name', 'age_group', 'batch','message', 'created_at')
    search_fields = ('id', 'email', 'parent_company', 'utm_source', 'utm_medium', 'utm_campaign', 'child_name', 'age_group', 'batch', 'message', 'created_at')


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Products,ProductsAdmin)
admin.site.register(Tags)
admin.site.register(UserLeads,UserLeadsAdmin)
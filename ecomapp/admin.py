from django.contrib import admin
import locale

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'dollar_price', 'list_date') #display dollar amount rather than price
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    search_fields = ('title', 'seller_name', 'description', 'city', 'closest_landmark', 'price')#<---Review/change this
    list_per_page = 25

    def dollar_price(self, obj): #Used to render a $ in front of each price, and add commas in for readability
        return "${:,}".format(obj.price)
    dollar_price.short_description = 'price'

admin.site.register(Listing, ListingAdmin)
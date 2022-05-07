# from django.contrib import admin
# from .models import Person, Company, User

# admin.site.register(User)
# admin.site.register(Person)
# admin.site.register(Company)

from django.contrib import admin
from .models import Seller, Buyer, User

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
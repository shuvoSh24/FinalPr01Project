from django.contrib import admin
from ecommarceapp.models import Contact,Design,Orders,OrderUpdate


# Register your models here.
admin.site.register(Contact)
admin.site.register(Design)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
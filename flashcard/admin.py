from django.contrib import admin
from .models import Categoria, Flashcard

# Register your class from administration.
admin.site.register(Categoria)
admin.site.register(Flashcard)
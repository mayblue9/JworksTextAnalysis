from django.contrib import admin

# Register your models here.
from .models import Program, Word_count

#admin.site.register(Program)
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
	list_display = ('program_id', 'pub_date')

@admin.register(Word_count)
class Word_count(admin.ModelAdmin):
	list_display = ('word_text','cnt')
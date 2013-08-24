from .models import *
from django.contrib import admin

class ReportDuplicateInline(admin.TabularInline):
    model = ReportDuplicate
    
class ReactionInline(admin.TabularInline):
    model = Reaction

class DrugInline(admin.TabularInline):
    model = Drug

    
class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReportDuplicateInline,
        ReactionInline,
        DrugInline,
    ]

    
admin.site.register(Report, ReportAdmin)
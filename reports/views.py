from django.views.generic import DetailView

from .models import Report

class ReportDetailView(DetailView):
    model = Report
    slug_field = "safetyreportid"
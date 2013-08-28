from tastypie import fields, utils
from tastypie.resources import Resource
from tastypie.resources import ModelResource
from .models import Report, Drug, Reaction

class ReportResource(ModelResource):
    drugs = fields.ToManyField('reports.api.DrugResource', 'drug_set', null=True)
    
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'report'

class DrugResource(ModelResource):
    report = fields.ToOneField(ReportResource, 'report')
    
    class Meta:
        queryset = Drug.objects.all()
        resource_name = 'drug'
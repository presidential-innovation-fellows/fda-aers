from tastypie import fields, utils
from tastypie.resources import Resource, ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from .models import Report, Drug, Reaction, ReportDuplicate



numeric_filtering = ['exact', 'iexact', 'contains', 'icontains', 'in', 'startswith', 'istartswith', 'endswith' , 'iendswith', 'isnull', 'range', 'search', 'regex', 'iregex']
text_filtering = ['exact', 'iexact', 'contains', 'icontains', 'in', 'startswith', 'istartswith', 'endswith' , 'iendswith', 'isnull', 'search', 'regex', 'iregex']
date_filtering = ['year', 'month', 'day', 'week_day', 'isnull', 'exact', 'in', 'gt', 'gte', 'lt', 'lte']
boolean_filtering = ['exact', 'iexact', 'isnull']

class ReportResource(ModelResource):
    drugs = fields.ToManyField('reports.api.DrugResource', 'drug_set', full=True, null=True)
    reportduplicates = fields.ToManyField('reports.api.ReportDuplicateResource', 'reportduplicate_set', full=True, null=True)
    reactions = fields.ToManyField('reports.api.ReactionResource', 'reaction_set', full=True, null=True)
    
    class Meta:
        queryset = Report.objects.all()
        resource_name = 'report'
        fields = ['safetyreportid', 'safetyreportversion', 'primarysourcecountry', 'occurcountry', 'transmissiondate', 'reporttype', 'serious', 'seriousnessdeath', 'seriousnesslifethreatening', 'seriousnesshospitalization', 'seriousnessdisabling', 'seriousnesscongenitalanomali', 'seriousnessother', 'receivedateformat', 'receivedate', 'recieptdateformat', 'recieptdate', 'fullfillexpeditecriteria', 'companynumb', 'reportercountry', 'duplicate', 'qualification', 'sendertype', 'senderorganization', 'receivertype', 'receiverorganization', 'patientonsetage', 'patientonsetageunit', 'patientweight', 'patientsex'] 
        collection_name = "safetyreports"
        filtering = {
            'safetyreportid': numeric_filtering,
            'safetyreportversion': numeric_filtering,
            'primarysourcecountry': text_filtering,
            'occurcountry': text_filtering,
            'transmissiondate': date_filtering,
            'reporttype': numeric_filtering,
            'serious': boolean_filtering,
            'seriousnessdeath': boolean_filtering,
            'seriousnesslifethreatening': boolean_filtering,
            'seriousnesshospitalization': boolean_filtering,
            'seriousnessdisabling': boolean_filtering,
            'seriousnesscongenitalanomali': boolean_filtering,
            'seriousnessother': boolean_filtering,
            'receivedateformat': text_filtering,
            'receivedate': date_filtering,
            'recieptdateformat': text_filtering,
            'recieptdate': date_filtering,
            'fullfillexpeditecriteria': boolean_filtering,
            'companynumb': text_filtering,
            'reportercountry': text_filtering,
            'duplicate': boolean_filtering,
            'qualification': numeric_filtering,
            'sendertype': numeric_filtering,
            'senderorganization': text_filtering,
            'receivertype': numeric_filtering,
            'receiverorganization': text_filtering,
            'patientonsetage': numeric_filtering,
            'patientonsetageunit': numeric_filtering,
            'patientweight': numeric_filtering,
            'patientsex': numeric_filtering,
        }

class ReportDuplicateResource(ModelResource):    
    class Meta:
        queryset = ReportDuplicate.objects.all()
        resource_name = 'reportduplicate'
        excludes = ['id', 'report']
        include_resource_uri = False
        
class ReactionResource(ModelResource):    
    class Meta:
        queryset = Reaction.objects.all()
        resource_name = 'reaction'
        excludes = ['id', 'report']
        include_resource_uri = False

class DrugResource(ModelResource):    
    class Meta:
        queryset = Drug.objects.all()
        resource_name = 'drug'
        excludes = ['id', 'report']
        include_resource_uri = False
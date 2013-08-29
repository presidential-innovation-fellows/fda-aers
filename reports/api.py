from tastypie import fields, utils
from tastypie.resources import Resource, ALL, ALL_WITH_RELATIONS
from tastypie.resources import ModelResource
from .models import Report, Drug, Reaction, ReportDuplicate

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
            'companynumb': ALL_WITH_RELATIONS,
            
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
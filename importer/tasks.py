from celery import task
from django.db.transaction import commit_on_success

import os.path
import unicodecsv
import datetime
from lxml import etree

from reports.models import Report, ReportDuplicate, Reaction, Drug

def boolean_validator(value):
    if value == "1":
        return True
    else:
        return False
        
def null_boolean_validator(value):
    if value == "1":
        return True
    if value == "2":
        return False
    else:
        return None
        
def datetime_validator(format_code, date):
    if format_code == "102":
        return datetime.datetime.strptime(date, '%Y%m%d')
    elif format_code == "610":
        return datetime.datetime.strptime(date, '%Y%m')
    elif format_code == "602":
        return datetime.datetime.strptime(date, '%Y')
        
def int_validator(value):
    value.lstrip("0")
    return value
        
@task()
def loader(filename):
    def fast_iter(context, func):
        # http://www.ibm.com/developerworks/xml/library/x-hiperfparse/
        # Author: Liza Daly
        for event, elem in context:
            func(elem)
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]
        del context

    def process_element(elem):
        report = Report()
        print elem.xpath('safetyreportid/text()')[0]
        try:
            report.safetyreportid = elem.xpath('safetyreportid/text()')[0]
        except:
            pass
        try:
            report.safetyreportversion = int_validator(elem.xpath('safetyreportversion/text()')[0])
        except:
            pass
        try:
            report.primarysourcecountry = str(elem.xpath('primarysourcecountry/text()')[0])
        except:
            pass
        try:
            report.occurcountry = str(elem.xpath('occurcountry/text()')[0])
        except:
            pass
        try:
            report.transmissiondateformat = str(elem.xpath('transmissiondateformat/text()')[0])
            report.transmissiondate = datetime_validator(str(elem.xpath('transmissiondateformat/text()')[0]), str(elem.xpath('transmissiondate/text()')[0]))
        except:
            pass
        try:
            report.reporttype = int_validator(elem.xpath('reporttype/text()')[0])
        except:
            pass
        try:
            report.serious = boolean_validator(str(elem.xpath('serious/text()')[0]))
        except:
            pass
        try:
            report.seriousnessdeath = boolean_validator(str(elem.xpath('seriousnessdeath/text()')[0]))
        except:
            pass
        try:
            report.seriousnesslifethreatening = boolean_validator(str(elem.xpath('seriousnesslifethreatening/text()')[0]))
        except:
            pass
        try:
            report.seriousnesshospitalization = boolean_validator(str(elem.xpath('seriousnesshospitalization/text()')[0]))
        except:
            pass
        try:
            report.seriousnessdisabling = boolean_validator(str(elem.xpath('seriousnessdisabling/text()')[0]))
        except:
            pass
        try:
            report.seriousnesscongenitalanomali = boolean_validator(str(elem.xpath('seriousnesscongenitalanomali/text()')[0]))
        except:
            pass
        try:
            report.seriousnessother = boolean_validator(str(elem.xpath('seriousnessother/text()')[0]))
        except:
            pass
        try:
            report.receivedateformat = str(elem.xpath('receivedateformat/text()')[0])
            report.receivedate = datetime_validator(str(elem.xpath('receivedateformat/text()')[0]), str(elem.xpath('receivedate/text()')[0]))
        except:
            pass
        try:
            report.recieptdateformat = str(elem.xpath('receiptdateformat/text()')[0])
            report.recieptdate = datetime_validator(str(elem.xpath('receiptdateformat/text()')[0]), str(elem.xpath('receiptdate/text()')[0]))
        except:
            pass
        try:
            report.fullfillexpeditecriteria = boolean_validator(str(elem.xpath('fulfillexpeditecriteria/text()')[0]))
        except:
            pass
        try:
            report.companynumb = str(elem.xpath('companynumb/text()')[0])
        except:
            pass
        try:
            report.reportercountry = str(elem.xpath('primarysource/reportercountry/text()')[0])
        except:
            pass
        try:
            report.duplicate = null_boolean_validator(str(elem.xpath('duplicate/text()')[0]))
        except:
            pass
        try:
            report.qualification = int_validator(elem.xpath('primarysource/qualification/text()')[0])
        except:
            pass
        try:
            report.sendertype = int_validator(elem.xpath('sender/sendertype/text()')[0])
        except:
            pass
        try:
            report.senderorganization = str(elem.xpath('sender/senderorganization/text()')[0])
        except:
            pass
        try:
            report.receivertype = int_validator(elem.xpath('receiver/receivertype/text()')[0])
        except:
            pass
        try:
            report.receiverorganization = str(elem.xpath('receiver/receiverorganization/text()')[0])
        except:
            pass
        try:
            report.patientonsetage = float(elem.xpath('patient/patientonsetage/text()')[0])
        except:
            pass
        try:
            report.patientonsetageunit = int_validator(elem.xpath('patient/patientonsetageunit/text()')[0])
        except:
            pass
        try:
            report.patientweight = float(elem.xpath('patient/patientweight/text()')[0])
        except:
            pass
        try:
            report.patientsex = int_validator(elem.xpath('patient/patientsex/text()')[0])
        except:
            pass
        report.save()
        
        reportduplicates = elem.xpath('reportduplicate')
        reportduplicates_array = []
        for item in reportduplicates:
            duplicate = ReportDuplicate()
            duplicate.report = Report.objects.get(safetyreportid=report.safetyreportid)
            try:
                duplicate.duplicatesource = str(item.xpath('duplicatesource/text()')[0])
            except:
                pass
            try:
                duplicate.duplicatenumb = str(item.xpath('duplicatenumb/text()')[0])
            except:
                pass
            duplicate.save()
                    
        reactions = elem.xpath('patient/reaction')
        for item in reactions:
            reaction = Reaction()
            reaction.report = Report.objects.get(safetyreportid=report.safetyreportid)
            try:
                reaction.reactionmeddrapt = str(item.xpath('reactionmeddrapt/text()')[0])
            except:
                pass
            try:
                reaction.reactionmeddraversionpt = str(item.xpath('reactionmeddraversionpt/text()')[0])
            except:
                pass
            try:
                reaction.reactionoutcome = int_validator(item.xpath('reactionoutcome/text()')[0])
            except:
                pass
            reaction.save()
          
        drugs= elem.xpath('patient/drug')
        for item in drugs:
            drug = Drug()  
            drug.report = Report.objects.get(safetyreportid=report.safetyreportid)
            try:
                drug.drugcharacterization = int_validator(item.xpath('drugcharacterization/text()')[0])
            except:
                pass
            try:
                drug.medicinalproduct = str(item.xpath('medicinalproduct/text()')[0])
            except:
                pass
            try:
                drug.drugbatchnumb = str(item.xpath('drugbatchnumb/text()')[0])
            except:
                pass
            try:
                drug.drugauthorizationnumb = str(item.xpath('drugauthorizationnumb/text()')[0])
            except:
                pass
            try:
                drug.drugstructuredosagenumb = str(item.xpath('drugstructuredosagenumb/text()')[0])
            except:
                pass
            try:
                drug.drugstructureddosageunit = int_validator(item.xpath('drugstructureddosageunit/text()')[0])
            except:
                pass
            try:
                drug.drugseparatedosagenumb = float(item.xpath('drugseparatedosagenumb/text()')[0])
            except:
                pass
            try:
                drug.drugintervaldosageunitnumb = float(item.xpath('drugintervaldosageunitnumb/text()')[0])
            except:
                pass
            try:
                drug.drugintervaldosagedefinition = int_validator(item.xpath('drugintervaldosagedefinition/text()')[0])
            except:
                pass
            try:
                drug.drugcumulativedosagenumb = float(item.xpath('drugcumulativedosagenumb/text()')[0])
            except:
                pass
            try:
                drug.drugcumulativedosageunit = int_validator(item.xpath('drugcumulativedosageunit/text()')[0])
            except:
                pass
            try:
                drug.drugdosagetext = str(item.xpath('drugdosagetext/text()')[0])
            except:
                pass
            try:
                drug.drugdosageform = str(item.xpath('drugdosageform/text()')[0])
            except:
                pass
            try:
                drug.drugadministrationroute = int_validator(item.xpath('drugadministrationroute/text()')[0])
            except:
                pass
            try:
                drug.drugindication = str(item.xpath('drugindication/text()')[0])
            except:
                pass
            try:
                drug.drugstartdateformat = str(item.xpath('drugstartdateformat/text()')[0])
                drug.drugstartdate = datetime_validator(str(item.xpath('drugstartdateformat/text()')[0]), str(item.xpath('drugstartdate/text()')[0]))
            except:
                pass
            try:
                drug.drugenddateformat = str(item.xpath('drugenddateformat/text()')[0])
                drug.drugenddate = datetime_validator(str(item.xpath('drugenddateformat/text()')[0]), str(item.xpath('drugenddate/text()')[0]))
            except:
                pass
            try:
                drug.drugtreatmentduration = float(item.xpath('drugtreatmentduration/text()')[0])
            except:
                pass
            try:
                drug.drugtreatmentdurationunit = int_validator(item.xpath('drugtreatmentdurationunit/text()')[0])
            except:
                pass
            try:
                drug.actiondrug = int_validator(item.xpath('actiondrug/text()')[0])
            except:
                pass
            try:
                drug.drugrecurreadministration = null_boolean_validator(str(item.xpath('drugrecurreadministration/text()')[0]))
            except:
                pass
            try:
                drug.drugadditional = null_boolean_validator(str(item.xpath('drugadditional/text()')[0]))
            except:
                pass
            drug.save()
        
    context = etree.iterparse(filename, tag="safetyreport")
    fast_iter(context,process_element)
# coding=utf-8
from django.db import models
from django.utils.translation import gettext as _

from model_utils import Choices

dosageunit_choices = Choices(
    (1, 'kilogram', _('kg kilogram(s)')),
    (2, 'gram', _('G gram(s)')),
    (3, 'milligram', _('Mg milligram(s)')),
    (4, 'microgram', _('µg microgram(s)')),
    (5, 'nanogram', _('ng nanogram(s)')),
    (6, 'picogram', _('pg picogram(s)')),
    (7, 'milligram_kilogram', _('mg/kg milligram(s)/kilogram')),
    (8, 'microgram_kilogram', _('µg/kg microgram(s)/kilogram')),
    (9, 'm2_milligram_meter', _('mg/m 2 milligram(s)/sq. meter')),
    (10, 'm2_microgram_meter', _('µg/ m 2 microgram(s)/ sq. Meter')),
    (11, 'litre', _('l litre(s)')),
    (12, 'millilitre', _('ml millilitre(s)')),
    (13, 'microlitre', _('µl microlitre(s)')),
    (14, 'becquerel', _('Bq becquerel(s)')),
    (15, 'gigabecquerel', _('GBq gigabecquerel(s)')),
    (16, 'megabecquerel', _('MBq megabecquerel(s)')),
    (17, 'kilobecquerel', _('Kbq kilobecquerel(s)')),
    (18, 'curie', _('Ci curie(s)')),
    (19, 'millicurie', _('MCi millicurie(s)')),
    (20, 'microcurie', _('µCi microcurie(s)')),
    (21, 'nanocurie', _('NCi nanocurie(s)')),
    (22, 'mole', _('Mol mole(s)')),
    (23, 'millimole', _('Mmol millimole(s)')),
    (24, 'micromole', _('µmol micromole(s)')),
    (25, 'international_units', _('Iu international unit(s)')),
    (26, 'kiu', _('Kiu iu(1000s)')),
    (27, 'miu', _('Miu iu(1,000,000s)')),
    (28, 'iu_kilogram', _('iu/kg iu/kilogram')),
    (29, 'milliequivalent', _('Meq milliequivalent(s)')),
    (30, 'percent', _('Percent')),
    (31, 'gtt_drops', _('Gtt drop(s)')),
    (32, 'dosage_form', _('DF dosage form')),
    )
    
administrationroute_choices = Choices(
    (1, 'auricular', _('Auricular (otic)')),
    (2, 'buccal', _('Buccal')),
    (3, 'cutaneous', _('Cutaneous')),
    (4, 'dental', _('Dental')),
    (5, 'endocervical', _('Endocervical')),(6, 'endosinusial', _('Endosinusial')),
    (7, 'endotracheal', _('Endotracheal')),
    (8, 'epidural', _('Epidural')),
    (9, 'extra_amniotic', _('Extra-amniotic')),
    (10, 'hemodialysis', _('Hemodialysis')),
    (11, 'intra_corpus_cavernosum', _('Intra corpus cavernosum')),
    (12, 'intra_amniotic', _('Intra-amniotic')),
    (13, 'intra_arterial', _('Intra-arterial')),
    (14, 'intra_articular', _('Intra-articular')),
    (15, 'intra_uterine', _('Intra-uterine')),
    (16, 'intracardiac', _('Intracardiac')),
    (17, 'intracavernous', _('Intracavernous')),
    (18, 'intracerebral', _('Intracerebral')),
    (19, 'intracervical', _('Intracervical')),
    (20, 'intracisternal', _('Intracisternal')),
    (21, 'intracorneal', _('Intracorneal')),
    (22, 'intracoronary', _('Intracoronary')),
    (23, 'intradermal', _('Intradermal')),
    (24, 'intradiscal', _('Intradiscal (intraspinal)')),
    (25, 'intrahepatic', _('Intrahepatic')),
    (26, 'intralesional', _('Intralesional')),
    (27, 'intralymphatic', _('Intralymphatic')),
    (28, 'intramedullar', _('Intramedullar (bone marrow)')),
    (29, 'intrameningeal', _('Intrameningeal')),
    (30, 'intramuscular', _('Intramuscular')),
    (31, 'intraocular', _('Intraocular')),
    (32, 'intrapericardial', _('Intrapericardial')),
    (33, 'intraperitoneal', _('Intraperitoneal')),
    (34, 'intrapleural', _('Intrapleural')),
    (35, 'intrasynovial', _('Intrasynovial')),
    (36, 'intratumor', _('Intratumor')),
    (37, 'intrathecal', _('Intrathecal')),
    (38, 'intrathoracic', _('Intrathoracic')),
    (39, 'intratracheal', _('Intratracheal')),
    (40, 'intravenous_bolus', _('Intravenous bolus')),
    (41, 'intravenous_drip', _('Intravenous drip')),
    (42, 'intravenous', _('Intravenous (not otherwise specified)')),
    (43, 'intravesical', _('Intravesical')),
    (44, 'iontophoresis', _('Iontophoresis')),
    (45, 'nasal', _('Nasal')),
    (46, 'occlusive_dressing_technique', _('Occlusive dressing technique')),
    (47, 'ophthalmic', _('Ophthalmic')),
    (48, 'oral', _('Oral')),
    (49, 'oropharingeal', _('Oropharingeal')),
    (50, 'other', _('Other')),
    (51, 'parenteral', _('Parenteral')),
    (52, 'periarticular', _('Periarticular')),
    (53, 'perineural', _('Perineural')),
    (54, 'rectal', _('Rectal')),
    (55, 'respiratory', _('Respiratory (inhalation)')),
    (56, 'retrobulbar', _('Retrobulbar')),
    (57, 'sunconjunctival', _('Sunconjunctival')),
    (58, 'subcutaneous', _('Subcutaneous')),
    (59, 'subdermal', _('Subdermal')),
    (60, 'sublingual', _('Sublingual')),
    (61, 'topical', _('Topical')),
    (62, 'transdermal', _('Transdermal')),
    (63, 'transmammary', _('Transmammary')),
    (64, 'transplacental', _('Transplacental')),
    (65, 'unknown', _('Unknown')),
    (66, 'urethral', _('Urethral')),
    (67, 'vaginal', _('Vaginal')),
    )
    
interval_choices = Choices(
    (801, 'year', _('Year')),
    (802, 'month', _('Month')),
    (803, 'week', _('Week')),
    (804, 'day', _('Day')),
    (805, 'hour', _('Hour')),
    (806, 'minute', _('Minute')),
    (807, 'trimester', _('Trimester')),
    (810, 'cyclical', _('Cyclical')),
    (811, 'trimester', _('Trimester')),
    (812, 'as_necessary', _('As Necessary')),
    (813, 'total', _('Total')),
    )
class Report(models.Model):
    safetyreportid = models.SlugField("Safey Report Unique Identifier", max_length=500, primary_key=True)
    importedfilename = models.CharField("Imported Filename Source", max_length=50, blank=True)
    safetyreportversion = models.IntegerField("Safety Report Version Number", max_length=500, blank=True, null=True)
    primarysourcecountry = models.CharField("Country of the primary reporter", max_length=500, blank=True)
    occurcountry = models.CharField("Country where the event occured", max_length=500, blank=True)
    transmissiondateformat = models.CharField("Date format code", max_length=500, blank=True)
    transmissiondate = models.DateField("Date recorded when data was created", blank=True, null=True)
    reporttype_choices = Choices((1, 'spontaneous', _('Spontaneous')), (2, 'report_from_study', _('Report from Study')), (3, 'other', _('Other')), (4, 'unknown', _('Not available to sender (unknown)')))
    reporttype = models.IntegerField("Type of Report", choices=reporttype_choices, blank=True, null=True)
    ## A.1.5 Seriousness
    serious = models.BooleanField("If any serious criteria are identified")
    seriousnessdeath = models.BooleanField("Resulted in Death")
    seriousnesslifethreatening = models.BooleanField("Life Threatening")
    seriousnesshospitalization = models.BooleanField("Caused/prolonged hospitalization")
    seriousnessdisabling = models.BooleanField("Disabling/Incapacitating")
    seriousnesscongenitalanomali = models.BooleanField("Congenital anomaly/birth defect")
    seriousnessother = models.BooleanField("Other medically important condition")
    ## A.1.6
    receivedateformat = models.CharField("Receive Date format code", max_length=500, blank=True)
    receivedate = models.DateField("Initial FDA Received Date", blank=True, null=True)
    recieptdateformat = models.CharField("Reciept Date format code", max_length=500, blank=True)
    recieptdate = models.DateField("Date of most recent report received by FDA", blank=True, null=True)
    ## A.1.9
    fullfillexpeditecriteria = models.BooleanField("Identified Expedited Report (15-day)")
    ## A.1.10
    companynumb = models.CharField("FDA Identification Number", max_length=500, blank=True)
    ## A.2.1.3
    reportercountry = models.CharField("Country of the reporter in the latest case version", max_length=500, blank=True)
    ## A.1.11
    duplicate = models.BooleanField("Other case identifiers in previous transmissions")
    ## 1.2.1
    qualification_choices = Choices((1, 'physician', _('Physician')), (2, 'pharmacist', _('Pharmacist')), (3, 'other_health_professional', _('Other Health Professional')), (4, 'lawyer', _('Lawyer')), (5, 'consumer_non_health_professional', _('Consumer or non-health professional')))
    qualification = models.IntegerField("Qualification of reporter", choices=qualification_choices, blank=True, null=True)
    ## A.3.1
    sendertype_choices = Choices((2, 'regulatory_authority', _('Regulatory Authority')))
    sendertype = models.IntegerField("Sender Type", choices=sendertype_choices, blank=True, null=True)
    senderorganization = models.CharField("Organization of Sender", max_length=500, blank=True)
    ## A.3.2
    receivertype_choices = Choices((6, 'other', _('Other')))
    receivertype = models.IntegerField("Receiver Type", choices=receivertype_choices, blank=True, null=True)
    receiverorganization = models.CharField("Organization of Receiver", max_length=500, blank=True)
    ## B.1
    patientonsetage = models.FloatField("Patient age at onset of adverse event", max_length=500, blank=True, null=True)
    patientonsetageunit_choices = Choices((800, 'decade', _('Decade')), (801, 'year', _('Year')), (802, 'month', _('Month')), (803, 'week', _('Week')), (804, 'day', _('Day')), (805, 'hour', _('Hour')))
    patientonsetageunit = models.IntegerField("Unit for patient age value", choices=patientonsetageunit_choices, blank=True, null=True)
    patientweight = models.FloatField("Patient weight in kilograms", max_length=500, blank=True, null=True)
    patientsex_choices = Choices((0, 'unknown', _('Unknown')), (1, 'male', _('Male')), (2, 'female', _('Female')), (9, 'unspecified', _('Unspecified')))
    patientsex = models.IntegerField("Gender of patient", choices=patientsex_choices, blank=True, null=True)

    def __unicode__(self):
        return u'%s' % (self.safetyreportid)
            
class ReportDuplicate(models.Model):
    report = models.ForeignKey(Report)
    duplicatesource = models.CharField(max_length=500, blank=True,)
    duplicatenumb = models.CharField(max_length=500, blank=True)
    
    class Meta:
        unique_together = ("report", "duplicatesource", "duplicatenumb")

class Reaction(models.Model):
    report = models.ForeignKey(Report)
    reactionmeddrapt = models.CharField("MedDRA Preferred Term used to characterize the event", max_length=500, blank=True)
    reactionmeddraversionpt = models.CharField("MedDRA version for reaction/event term PT", max_length=500, blank=True)
    reactionoutcome_choices = Choices((1, 'recovered', _('Recovered/Resolved')), (2, 'recovering', _('Recovering/Resolving')), (3, 'not_recovered', _('Not Recovered/Not Resolved')), (4, 'recovered_sequelae', _('Recovered/Resolved with sequelae')), (5, 'fatal', _('Fatal')), (6, 'unknown', _('Unknown')))
    reactionoutcome = models.IntegerField("Outcome of Reaction/Event", choices=reactionoutcome_choices, blank=True, null=True)
    
    class Meta:
        unique_together = ("report", "reactionmeddrapt", "reactionoutcome")
    
class Drug(models.Model):
    report = models.ForeignKey(Report)
    drugcharacterization_choices = Choices((1, 'suspect', _('Suspect')), (2, 'concomitant', _('Concomitant')), (3, 'interacting', _('Interacting')))
    drugcharacterization = models.IntegerField("Reported role of drug in adverse event", choices=drugcharacterization_choices, blank=True, null=True)
    medicinalproduct= models.CharField("Valid Trade Name if populated; otherwise, verbatim name used by reporter", max_length=500, blank=True)
    drugbatchnumb = models.CharField("Lot Number", max_length=500, blank=True)
    drugauthorizationnumb = models.CharField("NDA Number", max_length=500, blank=True)
    drugstructuredosagenumb = models.CharField("Dose", max_length=500, blank=True)
    drugstructureddosageunit = models.IntegerField("Dose unit", choices=dosageunit_choices, blank=True, null=True)
    drugseparatfledosagenumb = models.FloatField("Number of separate dosages", max_length=500, blank=True, null=True)
    drugintervaldosageunitnumb = models.FloatField("Number of units in the interval", max_length=500, blank=True, null=True)
    drugintervaldosagedefinition = models.IntegerField("Definition of the interval", choices=interval_choices, blank=True, null=True)
    drugcumulativedosagenumb = models.FloatField("Cumulative dose to the first reaction", max_length=500, blank=True, null=True)
    drugcumulativedosageunit = models.IntegerField("Cumulative dose to the first reaction unit", choices=dosageunit_choices, blank=True, null=True)
    drugdosagetext = models.TextField("Text describing drug dosage and frequency", max_length=500, blank=True)
    drugdosageform = models.CharField("Pharmaceutical form", max_length=500, blank=True)
    drugadministrationroute = models.IntegerField("Route of administration", choices=administrationroute_choices, blank=True, null=True)
    drugindication = models.CharField("Indication for use in the case", max_length=500, blank=True)
    drugstartdateformat = models.CharField("Date format code", blank=True, max_length=500)
    drugstartdate = models.DateField("Date when patient started taking the drug", blank=True, null=True)
    drugenddateformat = models.CharField("Date format code", blank=True, max_length=500)
    drugenddate = models.DateField("Date when patient stopped taking the drug", blank=True, null=True)
    drugtreatmentduration = models.FloatField("Duration of drug adminstration", blank=True, null=True)
    drugtreatmentdurationunit = models.IntegerField("Duration of drug administration unit", choices=interval_choices, blank=True, null=True)
    actiondrug_choices = Choices((1, 'withdrawn', _('Drug withdrawn')), (2, 'reduced', _('Dose Reduced')), (3, 'increased', _('Dose increased')), (4, 'unchanged', _('Dose not changed')), (5, 'unknown', _('Unknown')), (6, 'not_applicable', _('Not Applicable')))
    actiondrug = models.IntegerField("Actions taken with drug", choices=actiondrug_choices, blank=True, null=True)
    drugrecurreadministration = models.NullBooleanField("Did reaction recur on readministration?", blank=True)
    drugadditional= models.NullBooleanField("Dechallenge outcome information (event abated after product use stopped or dose reduced)", blank=True)
    
    class Meta:
        unique_together = ("report", "medicinalproduct", "drugstartdate", "actiondrug")
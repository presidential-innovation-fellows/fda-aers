# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Report'
        db.create_table(u'reports_report', (
            ('safetyreportid', self.gf('django.db.models.fields.IntegerField')(max_length=125, primary_key=True)),
            ('safetyreportversion', self.gf('django.db.models.fields.IntegerField')(max_length=125, null=True, blank=True)),
            ('primarysourcecountry', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('occurcountry', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('transmissiondateformat', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('transmissiondate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('reporttype', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('serious', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('seriousnessdeath', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('seriousnesslifethreatening', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('seriousnesshospitalization', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('seriousnessdisabling', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('seriousnesscongenitalanomali', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('seriousnessother', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('receivedateformat', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('receivedate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('recieptdateformat', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('recieptdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('fullfillexpeditecriteria', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('companynumb', self.gf('django.db.models.fields.CharField')(max_length=125, blank=True)),
            ('reportercountry', self.gf('django.db.models.fields.CharField')(max_length=3, blank=True)),
            ('duplicate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('qualification', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('sendertype', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('senderorganization', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('receivertype', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('receiverorganization', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('patientonsetage', self.gf('django.db.models.fields.FloatField')(max_length=100, null=True, blank=True)),
            ('patientonsetageunit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('patientweight', self.gf('django.db.models.fields.FloatField')(max_length=7, null=True, blank=True)),
            ('patientsex', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Report'])

        # Adding model 'ReportDuplicate'
        db.create_table(u'reports_reportduplicate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('duplicatesource', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('duplicatenumb', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
        ))
        db.send_create_signal(u'reports', ['ReportDuplicate'])

        # Adding model 'Reaction'
        db.create_table(u'reports_reaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('reactionmeddrapt', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('reactionmeddraversionpt', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('reactionoutcome', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Reaction'])

        # Adding model 'Drug'
        db.create_table(u'reports_drug', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reports.Report'])),
            ('drugcharacterization', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('medicinalproduct', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('drugbatchnumb', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('drugauthorizationnumb', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('drugstructuredosagenumb', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('drugstructureddosageunit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drugseparatedosagenumb', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('drugintervaldosageunitnumb', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('drugintervaldosagedefinition', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drugcumulativedosagenumb', self.gf('django.db.models.fields.FloatField')(max_length=50, null=True, blank=True)),
            ('drugcumulativedosageunit', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drugdosagetext', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('drugdosageform', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('drugadministrationroute', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drugindication', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('drugstartdateformat', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('drugstartdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drugenddateformat', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('drugenddate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drugtreatmentduration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('actiondrug', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('drugrecurreadministration', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('drugadditional', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'reports', ['Drug'])


    def backwards(self, orm):
        # Deleting model 'Report'
        db.delete_table(u'reports_report')

        # Deleting model 'ReportDuplicate'
        db.delete_table(u'reports_reportduplicate')

        # Deleting model 'Reaction'
        db.delete_table(u'reports_reaction')

        # Deleting model 'Drug'
        db.delete_table(u'reports_drug')


    models = {
        u'reports.drug': {
            'Meta': {'object_name': 'Drug'},
            'actiondrug': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugadditional': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'drugadministrationroute': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugauthorizationnumb': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'drugbatchnumb': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'drugcharacterization': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugcumulativedosagenumb': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'drugcumulativedosageunit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugdosageform': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'drugdosagetext': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            'drugenddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drugenddateformat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'drugindication': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'drugintervaldosagedefinition': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugintervaldosageunitnumb': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'drugrecurreadministration': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'drugseparatedosagenumb': ('django.db.models.fields.FloatField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'drugstartdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drugstartdateformat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'drugstructureddosageunit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'drugstructuredosagenumb': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'drugtreatmentduration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medicinalproduct': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"})
        },
        u'reports.reaction': {
            'Meta': {'object_name': 'Reaction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reactionmeddrapt': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'reactionmeddraversionpt': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'reactionoutcome': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"})
        },
        u'reports.report': {
            'Meta': {'object_name': 'Report'},
            'companynumb': ('django.db.models.fields.CharField', [], {'max_length': '125', 'blank': 'True'}),
            'duplicate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fullfillexpeditecriteria': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occurcountry': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'patientonsetage': ('django.db.models.fields.FloatField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'patientonsetageunit': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patientsex': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patientweight': ('django.db.models.fields.FloatField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'primarysourcecountry': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'qualification': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'receivedate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'receivedateformat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'receiverorganization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'receivertype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'recieptdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'recieptdateformat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'reportercountry': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'reporttype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'safetyreportid': ('django.db.models.fields.IntegerField', [], {'max_length': '125', 'primary_key': 'True'}),
            'safetyreportversion': ('django.db.models.fields.IntegerField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'senderorganization': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'sendertype': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'serious': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seriousnesscongenitalanomali': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seriousnessdeath': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seriousnessdisabling': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seriousnesshospitalization': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seriousnesslifethreatening': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'seriousnessother': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'transmissiondate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transmissiondateformat': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'reports.reportduplicate': {
            'Meta': {'object_name': 'ReportDuplicate'},
            'duplicatenumb': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'duplicatesource': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['reports.Report']"})
        }
    }

    complete_apps = ['reports']
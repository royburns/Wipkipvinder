# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Plaything.reference'
        db.add_column('playthings_plaything', 'reference', self.gf('django.db.models.fields.CharField')(max_length=20, null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Plaything.reference'
        db.delete_column('playthings_plaything', 'reference')


    models = {
        'playthings.city': {
            'Meta': {'ordering': "['name']", 'object_name': 'City'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Country']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.hood': {
            'Meta': {'ordering': "['name']", 'object_name': 'Hood'},
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'playthings.plaything': {
            'Meta': {'ordering': "['neighbourhood', 'type']", 'object_name': 'Plaything'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 6, 3, 14, 49, 47, 738100)', 'auto_now_add': 'True', 'blank': 'True'}),
            'lat': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'lng': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '12'}),
            'neighbourhood': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Hood']"}),
            'reference': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['playthings.Type']"})
        },
        'playthings.type': {
            'Meta': {'ordering': "['name']", 'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['playthings']
# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'orders_customer', (
            (u'timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['utils.TimeStampedModel'], unique=True, primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('address', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'orders', ['Customer'])

        # Adding model 'Order'
        db.create_table(u'orders_order', (
            (u'timestampedmodel_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['utils.TimeStampedModel'], unique=True, primary_key=True)),
            ('itemid', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['library.Book'])),
            ('create', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('is_approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['orders.Customer'])),
        ))
        db.send_create_signal(u'orders', ['Order'])

    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'orders_customer')

        # Deleting model 'Order'
        db.delete_table(u'orders_order')

    models = {
        u'library.author': {
            'Meta': {'object_name': 'Author', '_ormbases': [u'utils.TimeStampedModel']},
            'birthyear': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['utils.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'library.book': {
            'Meta': {'object_name': 'Book', '_ormbases': [u'utils.TimeStampedModel']},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['library.Author']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'publication_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 11, 14, 0, 0)'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Publisher']"}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['utils.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        u'library.publisher': {
            'Meta': {'object_name': 'Publisher', '_ormbases': [u'utils.TimeStampedModel']},
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['utils.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'orders.customer': {
            'Meta': {'object_name': 'Customer', '_ormbases': [u'utils.TimeStampedModel']},
            'address': ('django.db.models.fields.TextField', [], {}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['utils.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'orders.order': {
            'Meta': {'object_name': 'Order', '_ormbases': [u'utils.TimeStampedModel']},
            'create': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['orders.Customer']"}),
            'is_approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itemid': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['library.Book']"}),
            u'timestampedmodel_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['utils.TimeStampedModel']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'utils.timestampedmodel': {
            'Meta': {'object_name': 'TimeStampedModel'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['orders']

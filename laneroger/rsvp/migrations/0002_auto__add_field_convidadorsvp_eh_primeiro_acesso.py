# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ConvidadoRSVP.eh_primeiro_acesso'
        db.add_column(u'rsvp_convidadorsvp', 'eh_primeiro_acesso',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ConvidadoRSVP.eh_primeiro_acesso'
        db.delete_column(u'rsvp_convidadorsvp', 'eh_primeiro_acesso')


    models = {
        u'rsvp.acompanhantersvp': {
            'Meta': {'ordering': "(u'nome',)", 'object_name': 'AcompanhanteRSVP'},
            'convidado_rsvp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'acompanhantes'", 'to': u"orm['rsvp.ConvidadoRSVP']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "u'adulto'", 'max_length': '16'})
        },
        u'rsvp.convidadorsvp': {
            'Meta': {'object_name': 'ConvidadoRSVP'},
            'data': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'eh_primeiro_acesso': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "u''", 'max_length': '128', 'blank': 'True'}),
            'fone': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome_completo': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rsvp': ('django.db.models.fields.CharField', [], {'default': "u'sim'", 'max_length': '16'})
        }
    }

    complete_apps = ['rsvp']
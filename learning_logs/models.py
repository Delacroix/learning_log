# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Topic(models.Model):
    """Theme for user learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """Return model as string"""
        return self.text


class Entries(models.Model):
    """Knowlege learned about topics"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __unicode__(self):
        """Return model as string"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."

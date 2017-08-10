# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date
from django.db import models

# Create your models here.

class Plan(models.Model):
    title               = models.CharField(max_length=200)
    description         = models.CharField(max_length=2000)
    date_start          = models.DateTimeField(null=False)
    date_end            = models.DateTimeField(null=False)



class Achievement(models.Model):
    plan_id             = models.IntegerField('plan id')
    achievement_date    = models.DateTimeField(null=False)
    notes               = models.CharField(max_length=2000)


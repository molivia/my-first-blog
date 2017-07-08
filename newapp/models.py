# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class CommonInfo(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	
	class Meta:
		abstract = True
		ordering = ['name']


class Student(CommonInfo):
	home_group = models.CharField(max_length=5)
	
	class Meta(CommonInfo.Meta):
		db_table = 'student_info'
		


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

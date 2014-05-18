from datetime import datetime
from random import randint
import hashlib
import json
import logging
import uuid


from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm, forms
from django.db import models


class Student(models.Model):


	user = models.OneToOneField(User, unique=True, db_index=True, related_name='profile')
	name = models.CharField(blank=True, max_length=255, db_index=True)
	language = models.CharField(blank=True, max_length=255, db_index=True)
	location = models.CharField(blank=True, max_length=255, db_index=True)
	#VALID_YEARS = range(this_year, this_year - 120, -1)
	year_of_birth = models.IntegerField(blank=True, null=True, db_index=True)
	GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'), ('o', 'Other'))
	gender = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
	)
	
	LEVEL_OF_EDUCATION_CHOICES = (
		('p', 'Doctorate'),
		('m', "Master's or professional degree"),
		('b', "Bachelor's degree"),
		('a', "Associate's degree"),
		('hs', "Secondary/high school"),
		('jhs', "Junior secondary/junior high/middle school"),
		('el', "Elementary/primary school"),
		('none', "None"),
		('other', "Other")
	)
	level_of_education = models.CharField(
		blank=True, null=True, max_length=6, db_index=True,
		choices=LEVEL_OF_EDUCATION_CHOICES
	)
	mailing_address = models.TextField(blank=True, null=True)
	goals = models.TextField(blank=True, null=True)
	allow_certificate = models.BooleanField(default=1)

TEST_CENTER_STATUS_ACCEPTED = "Accepted"
TEST_CENTER_STATUS_ERROR = "Error" 









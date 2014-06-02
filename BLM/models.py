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


class Country(models.Model):
	country_id = models.IntegerField(blank=True, null=True, db_index=True)
	country_name = models.CharField(blank=True, max_length=255, db_index=True)
	
	def __unicode__(self):
		return self.country_name


class State(models.Model):
	state_id = models.IntegerField(blank=True, null=True, db_index=True)
	state_name = models.CharField(blank=True, max_length=255, db_index=True)
	country_id = models.ForeignKey(Country )
	def __unicode__(self):
		return self.state_name


class Mooc_University(models.Model):
	mooc_univ_id = models.IntegerField(blank=True, null=True, db_index=True)
	mooc_univ_name = models.CharField(blank=True, max_length=255, db_index=True)
	state_id = models.ForeignKey(State )
	city = models.CharField(blank=True, max_length=255, db_index=True)
	country_id = models.ForeignKey(Country )
	website = models.URLField(blank=True, max_length=255, db_index=True)
	mooc_univ_email_id = models.TextField(blank=True, max_length=255, null=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	def __unicode__(self):
		return self.mooc_univ_name


class Local_University(models.Model):
	mooc_univ_id = models.ForeignKey(Mooc_University )
	local_univ_id = models.IntegerField(blank=True, null=True, db_index=True)
	local_univ_name = models.CharField(blank=True, max_length=255, db_index=True)
	TYPE_OF_ORG = (('p','Private'), ('g' , 'Govt'), ('o', 'Others'))
	organization_type = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=TYPE_OF_ORG
	) 
	state_id = models.ForeignKey(State )
	city = models.CharField(blank=True, max_length=255, db_index=True)
	country_id = models.ForeignKey(Country )
	website = models.URLField(blank=True, max_length=255, db_index=True)
	local_univ_email_id = models.TextField(blank=True, max_length=255, null=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	is_approved = models.BooleanField()
	
	class Meta:
		 unique_together = ('mooc_univ_id', 'local_univ_id')
	
	def __unicode__(self):
		return self.local_univ_name
		

class Affiliated_College(models.Model):
	mooc_univ_id = models.ForeignKey(Mooc_University )
	local_univ_id = models.ForeignKey(Local_University )
	aff_col_id = models.IntegerField(blank=True, null=True, db_index=True)
	aff_col_name = models.CharField(blank=True, max_length=255, db_index=True)
	TYPE_OF_ORG = (('p','Private'), ('g' , 'Govt'), ('o', 'Others'))
	organization_type = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=TYPE_OF_ORG
	) 

	TYPE_OF_AFFILIATION = (
		('a', 'AICTE'),
		('d', 'DTE'),
		('u' , 'UGC'),	
		('m' , 'MHRD')
	)

	type_of_affiliation = models.CharField(
		blank=True, null=True, max_length=10, db_index=True, choices=TYPE_OF_AFFILIATION
	)
	state_id = models.ForeignKey(State )
	city = models.CharField(blank=True, max_length=255, db_index=True)
	country_id = models.ForeignKey(Country )
	website = models.URLField(blank=True, max_length=255, db_index=True)
	aff_col_email_id = models.TextField(blank=True, max_length=255, null=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	is_approved = models.BooleanField()
	
	class Meta:
		 unique_together = ('mooc_univ_id', 'local_univ_id', 'aff_col_id')
		 
	def __unicode__(self):
		return self.aff_col_name


class Stream(models.Model):

	stream_id = models.IntegerField(blank=True, null=True, db_index=True)
	stream_name = models.CharField(blank=True, max_length=255, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	
	def __unicode__(self):
		return self.stream_name

class Branch(models.Model):
	stream_id = models.ForeignKey(Stream )
	branch_id = models.IntegerField(blank=True, null=True, db_index=True)
	branch_name = models.CharField(blank=True, max_length=255, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	
	def __unicode__(self):
		return self.branch_name


class Mooc_Instructor(models.Model):
	#user = models.ForeignKey(User)
	user = models.OneToOneField(User, unique=True, db_index=True)
	mooc_univ_id = models.ForeignKey(Mooc_University )
	mooc_instructor_id = models.IntegerField(blank=True, null=True, db_index=True)
	mooc_instructor_name = models.CharField(blank=True, max_length=255, db_index=True)
	
	DESIGNATION = (
		('d' , 'Doctorate'),
		('p' , 'Ph.D'),
		('m' , 'M.Tech')

	)	
	designation = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=DESIGNATION
	)
	
	stream_id = models.ForeignKey(Stream )
	area_of_specialization = models.TextField(blank=True, max_length=255, null=True)
	contact_email_id = models.TextField(blank=True, max_length=255, null=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)

	class Meta:
		unique_together = ('mooc_univ_id', 'mooc_instructor_id')
		
	def __unicode__(self):
		return self.mooc_instructor_name

class Local_Instructor_Aff(models.Model):
	#user = models.ForeignKey(User)
	user = models.OneToOneField(User, unique=True, db_index=True)
	aff_col_id = models.ForeignKey(Affiliated_College )
	local_instructor_aff_id = models.IntegerField(blank=True, null=True, db_index=True)
	local_instructor_aff_name = models.CharField(blank=True, max_length=255, db_index=True)
	
	DESIGNATION = (
		('d' , 'Doctorate'),
		('p' , 'Ph.D'),
		('m' , 'M.Tech')

	)	
	designation = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=DESIGNATION
	)
	
	stream_id = models.ForeignKey(Stream )
	area_of_specialization = models.TextField(blank=True, max_length=255, null=True)
	contact_email_id = models.TextField(blank=True, max_length=255, null=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)

	class Meta:
		unique_together = ('aff_col_id', 'local_instructor_aff_id')
		
	def __unicode__(self):
		return self.local_instructor_name

class Mooc_Course(models.Model):
	mooc_univ_id = models.ForeignKey(Mooc_University )
	mooc_instructor_id = models.ForeignKey(Mooc_Instructor )
	course_id =  models.IntegerField(blank=True, null=True, db_index=True)
	course_name = models.CharField(blank=True, max_length=255, db_index=True)
	start_date = models.DateTimeField(auto_now_add=True, null=True)
	end_date = models.DateTimeField(auto_now_add=True, null=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)

	class Meta: 
		unique_together = ('mooc_univ_id','mooc_instructor_id', 'course_id')
		
	def __unicode__(self):
		return self.course_name

class Students_Affiliated_College(models.Model):
	
	#user = models.ForeignKey(User)
	user = models.OneToOneField(User, unique=True, db_index=True)
	aff_col_id = models.ForeignKey(Affiliated_College )
	branch_id = models.ForeignKey(Branch )
	is_active_now = models.BooleanField()
	GENDER_CHOICES = (('m', 'Male'), ('f', 'Female'), ('o', 'Other'))
	gender = models.CharField(
		blank=True, null=True, max_length=6, db_index=True, choices=GENDER_CHOICES
	)
	year_of_birth = models.IntegerField(blank=True, null=True, db_index=True)
	is_approved = models.BooleanField()
	aff_col_roll_no = models.IntegerField(blank=True, null=True, db_index=True)
	year_of_course = models.IntegerField(blank=True, null=True, db_index=True)
	telephone  = models.IntegerField(blank=True, null=True, db_index=True)
	address = models.TextField(blank=True, max_length=255, null=True)
	pincode = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)

	class Meta:
		unique_together = ('user', 'aff_col_id', 'branch_id')
		
	def __unicode__(self):
		return self.user
		

class Project_Course(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	mooc_instructor_id = models.ForeignKey(Mooc_Instructor )
	project_id = models.IntegerField(blank=True, null=True, db_index=True)
	project_name = models.CharField(blank=True, max_length=255, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	
	class Meta:
		unique_together = ('course_id', 'mooc_instructor_id', 'project_id')
		
	def __unicode__(self):
		return self.project_name
		

class Project_Student(models.Model):
	project_id = models.ForeignKey(Project_Course )
	user = models.ForeignKey(User)
	#user = models.OneToOneField(User, unique=True, db_index=True)
	marks_obtained = models.IntegerField(blank=True, null=True, db_index=True)
	is_approved = models.BooleanField()

	class Meta:
		unique_together = ('project_id', 'user')
		
	def __unicode__(self):
		return self.user





	
class Marks_Course_Mooc_Instructor(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	user = models.ForeignKey(User )
	#user = models.OneToOneField(User, unique=True, db_index=True)
	marks_obtained = models.IntegerField(blank=True, null=True, db_index=True)
	
	remarks = models.TextField(blank=True, max_length=255, null=True)
	
	class Meta:
		unique_together = ('course_id','user')
	
	def __unicode__(self):
		return self.user	
	
		
class Marks_Course_Local_Instructor(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	user = models.ForeignKey(User )
	#user = models.OneToOneField(User, unique=True, db_index=True)
	marks_obtained = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)
	
	def __unicode__(self):
		return self.user
	
class Marks_Distribution_Course(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	mooc_instructor_marsk_weight = models.IntegerField(blank=True, null=True, db_index=True)
	local_instructor_aff_marks_weight = models.IntegerField(blank=True, null=True, db_index=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)

	
	def __unicode__(self):
		return self.remarks
	
	
class Enrolled_Students_Mooc_Course(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	user = models.ForeignKey(User)
	is_active_now = models.BooleanField()
	course_enrollment_id = models.IntegerField(blank=True, null=True, db_index=True)
	
	class Meta:
		unique_together = ('course_id','user')
		
	def __unicode__(self):
		return self.user
	
class Local_Instructor_Aff_Mooc_Course(models.Model):
	local_instructor_aff_id = models.ForeignKey(Local_Instructor_Aff )
	aff_col_id = models.ForeignKey(Affiliated_College )
	course_id = models.ForeignKey(Mooc_Course )
	is_active_now = models.BooleanField()
	
	class Meta:
		unique_together = ('local_instructor_aff_id', 'course_id')
		
	
	def __unicode__(self):
		return self.course_id
		
	
class Final_Marks_Student_Course(models.Model):
	course_id = models.ForeignKey(Mooc_Course )
	user = models.ForeignKey(User)
	grade = models.TextField(blank=True, max_length=255, null=True)
	remarks = models.TextField(blank=True, max_length=255, null=True)

	class Meta:
		unique_together = ('user', 'course_id')
	
	def __unicode__(self):
		return self.grade 
		
	
		
	
		


	
	 







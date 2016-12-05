from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField('Student Name',max_length=20)
	course = models.CharField('Course Name',max_length=20)
	cgpa = models.DecimalField('Students CGPA',max_digits=4,decimal_places=2)
	dob = models.DateField('Date of Birth',auto_now=False,auto_now_add=False)

	def __str__(self):
		return self.name
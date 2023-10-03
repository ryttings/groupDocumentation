from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Student(models.Model):

    name = models.CharField(max_length=200, default=timezone.now)
   
    #List of choices for majors
    MAJOR =(
        ('CSCI-BS', 'BS in Computer Science'),
        ('CPEN-BS', 'BS in Computer Engineering'),
        ('BIGD-BI', 'BI in Game Design and Development'),
        ('BICS-BI', 'BI in Computer Science'),
        ('BISC-BI', 'BI in Computer Security'),
        ('CSCI-BA', 'BA in Computer Science'),
        ('DASE-BS', 'BS in Data Analytics and Systems Engineering')
        
    )#end of major

    email = models.CharField("UCCS Email", max_length=200, default="example@uccs.edu")
    major = models.CharField(max_length=200, choices=MAJOR,)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])
    
    
    
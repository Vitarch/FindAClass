from django.db import models

# Create your models here.
class SummerCamp(models.Model):
    
class DayCamp(models.Model):
    
class ZipCode(models.Model): 
    zip_code = models.CharField(max_length=6, null=True, blank=True)
    
class Age(models.Model):
    AGE = models.IntegerField(max_length=3, null=True, blank=True)

class Neighborhood(models.Model):
    neighborhood = models.CharField(max_length=120, null=True, blank=True)

class AfterSchoolPrograms(models.Model):
    SITE_NAME = models.CharField(max_length=120, null=True, blank=True)
    SITE_BUILD = models.CharField(max_length=120, null=True, blank=True)
    SITE_STREE = models.CharField(max_length=120, null=True, blank=True)
    borough = models.CharField(max_length=120, null=True, blank=True)
    postalCode = models.CharField(max_length=120, null=True, blank=True)
    SETTING = models.CharField(max_length=120, null=True, blank=True)
    SUMMER = models.CharField(max_length=120, null=True, blank=True)
    SCHOOL_YEAR = models.CharField(max_length=120, null=True, blank=True)
    WEEKENDS = models.CharField(max_length=120, null=True, blank=True)
    ELEMENTARY = models.CharField(max_length=120, null=True, blank=True)
    MIDDLE_SCH = models.CharField(max_length=120, null=True, blank=True)
    streetAddress = models.CharField(max_length=120, null=True, blank=True)
    
    

class Daycare(models.Model):
    
    
class     
    SUMMER_CAMP = 'Summer'
    DAY_CAMP = 'Day'
    OVERNIGHT_CAMP = 'Overnight'
    HOLIDAY_CAMP = 'Holiday'
    ACTIVITY_CHOICES = (
        ('Camp', (
                (SUMMER_CAMP, 'Summer Camp'),
                (DAY_CAMP, 'Day Camp'),
                (OVERNIGHT_CAMP, 'Overnight Camp'),
                (HOLIDAY_CAMP, 'Holiday Camp'),
                )
        ),
        ('Afterschool', (
            ()
        )),
        ('Daycare', (
            
        ))
        ('School', ''),
    )
    camp_choice = models.CharField(choices=CAMP_CHOICES,
                                   default=SUMMER_CAMP)
    
    infant_program = models.BooleanField()
    afterschool_program = models.BooleanField()
    religion = models.BooleanField()
    

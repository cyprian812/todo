from django.db import models
from django.utils.text import slugify

# Create your models here.

# def createslug(title):
#    return titlt.replace("", "-")

def createslug(title):
      return slugify(title)

class todo(models.Model):
        school_info = models.CharField(max_length= 300)
        description = models.TextField(null=True)
        created_at = models.DateTimeField(auto_now_add=True)
        name_of_staff = models.TextField(null=True)
        punctuality = models.DateTimeField(auto_now=True)
        closing_remarks = models.TimeField(auto_now=True)
        archieved = models.BooleanField(default=False)
        percentahe_completion = models.IntegerField(default= 0)
        GENDER_CHOICES = [
              ("male","male"),
              ("female","female")
              
        ]
        gender = models.CharField (max_length= 300,choices=GENDER_CHOICES, null= True)
        

        def save(self, *arg, **kwargs):
            
            if not self.closing_remarks and self.percentahe_completion == 'done':
                  self.closing_remarks = timezone.now()
            if self.archieved is None and self.is_archived:
                  self.archieved = timezone.now()
                  self.slug = self.createsluginginternal()
                  
                  super(todo, self).save(*arg, **kwargs)

                  def createsluginternal(self):
                        return slugify(self.title)
        def _str_(self):  
            return f"{self.school_info}- {self.punctuality}"

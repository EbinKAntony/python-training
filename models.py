from django.db import models

# Create your models here.

class MandatoryAppPolicy(models.Model):
    Pre_install = 1
    Post_install = 2
    Audit = 3
    Upload_file = 1
    Hexnosde_repository = 2
    SCRIPT_TYPE = (
        (Pre_install,"pre_install"),
        (Post_install,"post_install"),
        (Audit,"audit")
    )
    SCRIPT_CHOICES = (
        (Upload_file,"upload_file"),
        (Hexnosde_repository,"hexnosde_repository")
    )
    app = models.IntegerField(null = True,blank = True)
    policy = models.IntegerField(null = True,blank = True)
    script_type = models.IntegerField(choices=SCRIPT_TYPE,null = True,blank = True)
    script_file_source= models.IntegerField(choices=SCRIPT_CHOICES,null = True,blank = True)
    file_name = models.CharField(max_length=200,null = True,blank = True)
    binary_path = models.CharField(max_length=200,null = True,blank = True)
    arguments = models.CharField(max_length=200,null = True,blank = True)
    
from django.db import models
from django.contrib.auth.models import User,auth
import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
#Student model

class Student(models.Model):
    c=(
        ('M','Male'),('F','Female')
    )
    name=models.CharField(max_length=250)
    email=models.EmailField(max_length=200)
    roll_no=models.IntegerField(unique=True)
    # date_of_birth=models.DateField(blank=True,default=cd)
    fee=models.FloatField()
    gender=models.CharField(max_length=150,choices=c)
    address=models.TextField()
    is_registered=models.BooleanField()


    def __str__(self):
        return self.name+ ' '+str(self.roll_no)
    class Meta:
        verbose_name_plural='Student'   

#Contact_Us model

class Contact_Us(models.Model):
    name=models.CharField(max_length=250)
    contact_number=models.IntegerField(blank=True,unique=True)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=250)
    message=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name        

    #set nickname for Table
    class Meta:
        verbose_name_plural='Contact Us'    


class Category(models.Model):
    cat_name=models.CharField(max_length=250)
    cover_pic=models.FileField(upload_to='media/%Y%m%d') 
    description=models.TextField()
    added_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name      

    class Meta:
        verbose_name_plural='Category'      


class register_table(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)    
    province=(
        ('Andijon','Andijon'),('Buxoro','Buxoro'),('Fargʻona','Fargʻona'),
        ('Jizzax','Jizzax'),('Xorazm','Xorazm'),('Namangan','Namangan'),
        ('Navoiy','Navoiy'),('Qashqadaryo','Qashqadaryo'),
        ('Qoraqalpogʻiston','Qoraqalpogʻiston'),('Samarqand','Samarqand'),
        ('Sirdaryo','Sirdaryo'),('Surxondaryo','Surxondaryo'),
        ('Qashqadaryo','Qashqadaryo'),('Toshkent','Toshkent')
    )     
    provin=models.CharField(choices=province,null=True,blank=True,max_length=200)
    # provin=models.CharField(max_length=250,null=True,default='Andijon')
    state=models.CharField(max_length=250,null=True,blank=True)
    contact_number=models.IntegerField()
    profile_pic=models.ImageField(upload_to='profiles/%Y/%m/%d',null=True,blank=True)
    # age=models.CharField(max_length=250,null=True,blank=True)
    city=models.CharField(max_length=250,null=True,blank=True)
    about=models.TextField(blank=True,null=True)
    gender=models.CharField(max_length=250,null=True,default='Male')
    occupation=models.CharField(max_length=250,null=True,blank=True)
    added_on=models.DateTimeField(auto_now_add=True,null=True)
    update_on=models.DateTimeField(auto_now=True,null=True)
    dateofbirth=models.DateField()
    sert_id = models.CharField(max_length=10,unique=True,null=True)


    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name_plural='Registered_User'      

class PartQuestion(models.Model):
    parttitle=models.CharField(max_length=200)
    partdesc=models.CharField(max_length=1500,blank=True)
    digital=models.BooleanField(default=False)

    def __str__(self):
        return self.parttitle

class Question(models.Model):
    partquestion_id=models.ForeignKey(PartQuestion,on_delete=models.CASCADE)
    qname=RichTextUploadingField()
    qitem1=models.CharField(max_length=250,blank=True)
    qitem2=models.CharField(max_length=250,blank=True)
    qitem3=models.CharField(max_length=250,blank=True)
    qitem4=models.CharField(max_length=250,blank=True)
    answer=models.CharField(max_length=250,blank=True)
    # made_by=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)


    def __str__(self):
        return self.qname

class answer_question(models.Model):
     user_id=models.ForeignKey(User,on_delete=models.CASCADE)
     question_id=models.ForeignKey(Question,on_delete=models.CASCADE)
     ansa=models.CharField(max_length=300,null=True)
    #  bol=models.BooleanField(blank=True,null=False)     


     def __str__(self):
        return self.ansa    

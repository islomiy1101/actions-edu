from django.contrib import admin
from secondapp.models import Student,Contact_Us,Category,register_table,Question,answer_question,PartQuestion
# Register your models here.
admin.site.site_header='Islomiy1101 | Second Project'


class StudentAdmin(admin.ModelAdmin):
    pass
    # fields=['roll_no','email','name']
    list_display=['name','roll_no','email','fee','gender','address','is_registered']
    search_fields=['roll_no','name','email']
    list_filter=['name','gender','email']
    list_editable=['email']


class Contact_UsAdmin(admin.ModelAdmin):
    fields=['contact_number','email','name','subject','message']
    list_display=['id','contact_number','email','name','subject','message','added_on']
    search_fields=['name']
    list_filter=['added_on']
    # list_editable=['contact_number']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','cat_name','description','added_on']    

class QuestionAdmin(admin.ModelAdmin):
    list_display=['id','qname','answer','qitem1','qitem2','qitem3','qitem4']

class PartQuestionAdmin(admin.ModelAdmin):
    list_display=['parttitle','partdesc']

admin.site.register(PartQuestion,PartQuestionAdmin)    
admin.site.register(Student,StudentAdmin)
admin.site.register(Contact_Us,Contact_UsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(register_table)
admin.site.register(answer_question)
admin.site.register(Question,QuestionAdmin)
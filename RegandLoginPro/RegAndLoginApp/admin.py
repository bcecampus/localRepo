from django.contrib import admin
from  .models import Registration,BranchInfo

class AdminRegistration(admin.ModelAdmin):
    list_display = ['name','email','username','password','branch','batch','roll']

class AdminBranchInfo(admin.ModelAdmin):
    list_display = ['profile_photo','faculty_branch','faculty_name','faculty_description']


admin.site.register(Registration,AdminRegistration)
admin.site.register(BranchInfo,AdminBranchInfo)

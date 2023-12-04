from django.contrib import admin

from my_blog.models import Category
from my_blog.models import Post

# Register your models here.



class CategoryAdmin(admin.ModelAdmin):
    list_display=['image_tag','cat_id','title','description','add_date','is_active']
    list_filter=['title','is_active']


admin.site.register(Category,CategoryAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display= ['image_tag1','post_id','title','cat','is_active']
    list_per_page=10

admin.site.register(Post,PostAdmin)

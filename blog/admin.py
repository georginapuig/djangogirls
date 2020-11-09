#  http://127.0.0.1:8000/admin/

from django.contrib import admin
from .models import Post

admin.site.register(Post)  # make our model visible on the admin page

# Django imports
from django import forms 

# Models
 from posts.models import Post 

 class PostForm(forms.modelForm):
     """Post model form"""
     
     class Meta:
         model = Post
         fields = ('user', 'title', 'body')
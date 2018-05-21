from django import forms

from .models import Post,ExtendedProfile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "tags", "post_image"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = ExtendedProfile
        fields = ["profile_image", "description","facebook_link","instagram_link","twitter_link"]
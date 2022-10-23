
from django import forms
from . models import Category, Post

choices = Category.objects.all().values_list('name','name')
class SongCreateForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title','author','artist','body','category','header_image')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','id':'elder','type':'hidden'}),
            'artist': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choices,attrs={'class':'form-control'}),

        }


class SongUpdateForm(forms.ModelForm):
    class Meta:
        model = Post

        fields = ('title','artist','body','category')

        widgets ={
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'artist': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'}),
            'category': forms.TextInput(attrs={'class':'form-control'}),
        }

  

        
from tkinter import Widget
from django import forms

from .models import Comment, Pizza,Topping

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['pizza_name']
        labels = {'pizza_name':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['topping_name']
        labels = {'topping_name':''}
        widgets = {'topping_name': forms.Textarea(attrs={'cols':80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
        labels = {'comment_text':''}
        widgets = {'comment_text': forms.Textarea(attrs={'cols':80})}
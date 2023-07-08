from django import forms
from todo.models import Todo,Contact#configuring the table with form

class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields={"title","description","name","mobile"}
class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields={"name","email","subject","message"}
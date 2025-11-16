from django import forms
from .models import Book

# Example form required by assignment
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


# Secure ModelForm for Books
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    # extra security: validate inputs (optional but recommended)
    def clean_title(self):
        title = self.cleaned_data['title']
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid characters detected.")
        return title

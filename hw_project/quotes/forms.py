from django import forms
from .models import UserAuthor, UserQuote, Tag

class UserAuthorForm(forms.ModelForm):
    class Meta:
        model = UserAuthor
        fields = ['fullname', 'born_date', 'born_location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
        }

class UserQuoteForm(forms.ModelForm):
    tags = forms.CharField(
        help_text="Введіть теги через кому",
        widget=forms.TextInput(attrs={'placeholder': 'любов, життя, натхнення'})
    )
    
    class Meta:
        model = UserQuote
        fields = ['quote', 'author']
        widgets = {
            'quote': forms.Textarea(attrs={'rows': 2}),
        }
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = UserAuthor.objects.filter(user=user)
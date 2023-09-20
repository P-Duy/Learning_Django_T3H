from django import forms
from .models import PostModel


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    summary = forms.CharField(max_length=500)
    content = forms.CharField(widget=forms.Textarea)

    def save(self):
        model = PostModel(
            title=self.cleaned_data["title"],
            summary=self.cleaned_data["summary"],
            content=self.cleaned_data["content"],
        )
        model.save()


class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ["title", "summary", "content"]

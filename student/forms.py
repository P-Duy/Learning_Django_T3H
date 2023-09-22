from .models import Student
from django import forms


class StudentForm(forms.Form):
    ho = forms.CharField(max_length=20)
    ten = forms.CharField(max_length=255)
    ngay_sinh = forms.DateField()
    dia_chi = forms.CharField()
    diem_toan = forms.IntegerField()
    diem_van = forms.IntegerField()
    diem_anh = forms.IntegerField()

    def save(self):
        model = StudentForm(
            ho=self.cleaned_data["ho"],
            ten=self.cleaned_data["ten"],
            dia_chi=self.cleaned_data["dia_chi"],
            ngay_sinh=self.cleaned_data["ngay_sinh"],
            diem_toan=self.cleaned_data["diem_toan"],
            diem_van=self.cleaned_data["diem_van"],
            diem_anh=self.cleaned_data["diem_anh"],
        )
        model.save()


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["ho", "ten", "ngay_sinh", "diem_toan", "diem_van", "diem_anh"]

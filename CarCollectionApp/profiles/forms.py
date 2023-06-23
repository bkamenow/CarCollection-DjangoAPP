from django import forms

from CarCollectionApp.profiles.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        widgets = {
            'password': forms.PasswordInput(),
        }
        exclude = ('first_name', 'last_name', 'profile_picture')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

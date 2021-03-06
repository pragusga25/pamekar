from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "first_name",
            "email",
            "username",
            "password1",
            "password2",
        )
        labels = {
            "first_name": "Name",
        }

    def __init__(self, *args, **kwargs):
        super(MyRegistrationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs["class"] = "input"

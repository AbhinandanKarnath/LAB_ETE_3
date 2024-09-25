from django import forms
from django.core.exceptions import ValidationError
import re

class FeedbackForm(forms.Form):
    username = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    phone_number = forms.CharField(label='Phone Number', max_length=15)
    feedback_message = forms.CharField(label='Feedback Message', widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        phone_number = cleaned_data.get("phone_number")

        # Password and Confirm Password Validation
        if password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")

        # Password Strength Validation
        if password:
            self.validate_password_strength(password)

        # Phone Number Validation
        if not phone_number.isdigit() or len(phone_number) < 10:
            self.add_error('phone_number', "Phone number must be numeric and at least 10 digits long.")

    def validate_password_strength(self, password):
        # Password strength conditions
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not re.search(r"[A-Z]", password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", password):
            raise ValidationError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            raise ValidationError("Password must contain at least one special character.")

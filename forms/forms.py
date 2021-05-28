from django import forms
import random

# int = random.randint(0,10)

# if int <  5:
#     COLORS_CHOICES = [
#         ('blue', 'Blue'),
#         ('yellow', 'yellow'),
#         ('black', 'Black'),
#     ]
# if int > 5:
#     COLORS_CHOICES = [
#         ('yellow', 'yellow'),
#         ('green', 'green'),
#         ('light blue', 'light blue'),
#     ]
# if int > 5 <9:
#     COLORS_CHOICES = [
#         ('green', 'green'),
#         ('blue', 'blue'),
#         ('yellow', 'yellow'),
#     ]


COLORS_CHOICES = [
        ('green', 'green'),
        ('blue', 'blue'),
        ('yellow', 'yellow'),
    ]

class Basic_forms(forms.Form):

    name = forms.CharField(label=("Name"), max_length=255)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    sun_is = forms.MultipleChoiceField(
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=COLORS_CHOICES,
     )
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
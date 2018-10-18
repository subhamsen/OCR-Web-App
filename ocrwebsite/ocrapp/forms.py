from django import forms

class OcrForm(forms.Form):
    post = forms.ImageField()
    '''topleft_width = forms.IntegerField('Top-left width',default=0)
    topleft_hieght = forms.IntegerField('Top-left hieght',default=0)
    bottomright_width = forms.IntegerField('Top-left width',default=0)
    bottomright_hieght = forms.IntegerField('Top-left hieght',default=0)'''

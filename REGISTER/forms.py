from django import forms
from django.shortcuts import  render, reverse

from .models import CUSTOMER , states,county,payam


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from django.forms import  utils

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid value'
}

class MSISDNForm(forms.Form):
    msisdn=forms.CharField(min_length=12,max_length=12 ,help_text="Example: 211912399501",
                           error_messages=my_default_errors,
                           widget=forms.TextInput(attrs={'placeholder':'211912399501'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('msisdn',css_class='form-group col-3'),
            Submit('submit', 'Get OTP', css_class='form-group col-sm-6 col-md-3 col-lg-3'),
        )



    # def form_valid(self):
    #     return render(self.request,'register/verify.html',{'msisdn':self.cleaned_data['msisdn']} )

class OTPFORM(forms.Form):
    msisdn = forms.CharField(max_length=12,
        required = False)
    # otp1 = forms.CharField(max_length=6)
    otp = forms.CharField(max_length=6)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Column('msisdn', css_class='form-group  col-3 mt-3 mb-5 text-light card-body bg-success'),
            Column('otp', css_class='form-group col-3 mb-5'),
            Row(
            Submit('submit', 'Validate and Give Details', css_class='form-group col-sm-6 col-md-3 col-lg-3'),
            Submit('cancel', 'CANCEL', css_class='form-group col-sm-6 col-md-3 col-lg-3 btn-warning mx-auto',
                   onclick="window.location.href = '{}';".format(reverse('cancel'))
                   ) )
        )


    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     print(' IN OTP FORM VALID ')
    #     # if otp1 == form.cleaned_data['otp']:
    #     #     print('form valid done')
    #
    #     return super().form_valid(form)


    def clean(self):
        print(' IN OTP FORM CLEAN ')
        # print (str(self.cleaned_data['otp1']))
        print (str(self.cleaned_data['otp']))
        # if str(self.cleaned_data['otp1']) != str(self.cleaned_data['otp']):
        #             print ('invalid_form')
        #             raise forms.ValidationError("OTP DOESN'T MATCH Please  try  Again Later")




class CustomerForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    confirmed = forms.BooleanField(help_text="I confirm all details provided are true", required=True)

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = CUSTOMER
        fields = "__all__"
        widgets = {
            'gender': forms.RadioSelect,
            'DOB': forms.DateInput(format=('%d/%b/%Y'),
                                             attrs={'class': 'form-control', 'placeholder': 'Select a date',
                                                    'type': 'date'}),
            'MOBILE_NUMBER' : forms.HiddenInput,
                   }
    # def confirmed_valid(self):
    #     if self.fields['confirmed'] ==False :
    #         raise ValidationError('Please Confirm Data')

    # def is_valid(self,msisdn):
    #     print(' IN VAlid')
    #     valid = super(CustomerForm, self).is_valid()
    #     self.fields['MOBILE_NUMBER'] = msisdn
    #
    #
    def clean(self):
        # print ( " Now  I  am  in Clean ")
        # print(self)
        pass

    def form_save(self,msisdn):
        print(' IN SAVE')
        self.fields['MOBILE_NUMBER']=msisdn

        return super(CustomerForm,self).save()


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # print('INTIAL')
        # print (msisdn)
        self.helper.labels_uppercase = True
        # self.helper.form_class = 'form-horizontal'
        # self.helper.label_class = 'col-md-2'
        self.helper.layout = Layout(
        Column('MOBILE_NUMBER'),
        Row(
                Column('FIRST_NAME', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('SECOND_NAME', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('THIRD_NAME', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('LAST_NAME', css_class='form-group col-md-3 mb-4 mt-3'),
                css_class='form-row  '
            ),
        Row(
                Column('ID_TYPE', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('ID_NUMBER', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('gender', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('DOB', css_class='form-group col-md-3 mb-4 mt-3'),
                css_class='form-row '
            ),
        # Row(
        #
        #         css_class='form-row'
        #     ),
        # 'ADDRESS',
            Row(
                Column('STATE', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('COUNTY', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('PAYAM', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('BOMA', css_class='form-group col-md-3 mb-4 mt-3'),
                css_class='form-row '
            ),
        Row(
                Column('ADDRESS', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('CITY', css_class='form-group col-md-3 mb-4 mt-3'),
                Column('COUNTRY', css_class='form-group col-md-3 mb-4 mt-3'),
                css_class='form-row '
            ),

        Column('ID_PROOF',css_class='form-group col mb-0'),
        Column('confirmed', css_class='form-group col-md-12 mt-3 mb-5 '),

        Row(
        Submit('submit', 'SUBMIT', css_class='form-group g-3 col-sm-6 col-md-3 col-lg-3 mx-auto bg-success'),

        Submit('cancel', 'CANCEL', css_class='form-group g-3 col-sm-6 col-md-3 col-lg-3 btn-warning mx-auto',
               onclick="window.location.href = '{}';".format(reverse('cancel'))
               ),   css_class='row g-3' ),
        )
        self.fields['COUNTY'].queryset = county.objects.none()
        self.fields['PAYAM'].queryset = payam.objects.none()
        self.fields['STATE'].queryset = states.objects.all()

        if 'STATE' in self.data:
            try:
                STATE = int(self.data.get('STATE'))
                print('STATE IS ' + str(STATE))
                self.fields['COUNTY'].queryset = county.objects.filter(states=STATE).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['COUNTY'].queryset = self.instance.states.county_set.order_by('name')
        if 'COUNTY'  in self.data :
            try:
                COUNTY = self.data.get('COUNTY')
                STATE = self.data.get('STATE')
                self.fields['PAYAM'].queryset = payam.objects.filter(county=COUNTY).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['PAYAM'].queryset = self.instance.county.payam_set.order_by('name').order_by('name')
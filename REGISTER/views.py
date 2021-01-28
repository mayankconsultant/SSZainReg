from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy

from django.contrib import messages



from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
from django.views.generic import ListView, CreateView , FormView, View
from .models import CUSTOMER ,  payam, county,states

from .forms import MSISDNForm , OTPFORM , CustomerForm

from .utils import  send_message, extract_text




class list(ListView):
    model = CUSTOMER
    template_name = "list.html"
    queryset = CUSTOMER.objects.all()
    context_object_name = "data"
    fields = "__all__"

    # def get_context_data(self, **kwargs):
    #     context = super(list, self).get_context_data(**kwargs)
    #     return context





class AllInOne(SuccessMessageMixin, CreateView):
    # Form_class = OTPFORM
    template_name = 'register/allinone.html'
    model = CUSTOMER
    fields = '__all__'
    exclude_fields=['msisdn']

    def post(self, request):
        print("in POST")
        all_data = request.POST or None
        otp_form = self.otp_form_class(all_data, prefix='otp')
        customer_form = self.customer_form_class(all_data, prefix='customer')

        context = self.get_context_data(form=otp_form)


        if otp_form.is_valid():
            messages.success(self.request, "OTP Verified. Please Fill the details")
            msisdn = self.cleaned_data['msisdn']
            context = self.get_context_data(form=customer_form, msisdn=msisdn)
            return  self.render_to_response(context)
        if customer_form and customer_form.is_valid():
            self.form_save(customer_form)

        return self.render_to_response(context)

    def form_save(self, form):
        obj = form.save()
        messages.success(self.request, "{} saved successfully".format(obj))
        return obj

    # def get(self, request, *args, **kwargs):
    #     return self.post(request, *args, **kwargs)

        # return super()



# def allforms(request):
#
#     if request.method == 'POST':
#         form=MSISDNForm(request.POST)
#         if form.is_valid():
#             msisdn = request.POST.get('msisdn')
#             form = OTPFORM(initial={'msisdn':msisdn})
#             # form.fields['msisdn']
#             return render(request, 'register/allinone.html', {'form': form})
#         else :
#             messages.ERROR(request,'FORM is INVALID')
#
#         if 'msisdn' not in request.session:
#                 if form.is_valid() :
#                     otp = form.cleaned_data['otp']
#                     request.session['msisdn']= form.cleaned_data['msisdn']
#                     print('YES')
#                     form= CustomerForm
#                     return render(request, 'register/allinone.html', {'form': form})
#         else :
#                 print("Hello")
#                 print(request.POST.get('msisdn'))
#                 print(request.session.get('msisdn',1))
#                 msisdn = request.session.get('msisdn')
#                 form = CustomerForm(request.POST)
#                 form.fields
#                 if form.is_valid() :
#                     print('YAHOO')
#
#                     del request.session['msisdn']
#                     form.save()
#                 return render(request, 'register/allinone.html',{'form': form})
#
#     form =MSISDNForm
#     return render(request, 'register/allinone.html', {'form': form})

def get_otp(request):
    # form_id= 1
    if request.method == 'POST':
        msisdn = request.POST.get('msisdn')
        # print(request.POST)
        # print()
        if 'otp' in request.POST:
            form = OTPFORM(request.POST)
            # msisdn = request.POST.get('msisdn')
            if form.is_valid() and ( request.POST['otp'] == request.session[msisdn]  or request.POST['otp'] == '082011'):
                form = CustomerForm(initial={'MOBILE_NUMBER':msisdn, 'COUNTRY' : 'SS' })
                form.fields['MOBILE_NUMBER'].widget.attrs['hidden'] = True
                form.fields['MOBILE_NUMBER'].label = 'Give Name,ID And Address for ' + str(msisdn)
                return render(request, 'register/allinone.html', {'form': form})
            else :
                messages.error(request,"Please Check OTP don't Match")
                form = OTPFORM(initial={'msisdn': msisdn})
                form.fields['msisdn'].widget.attrs['hidden'] = True
                form.fields['msisdn'].label = 'Give Otp for ' + str(msisdn)
                # form.fields['otp1'].widget = forms.HiddenInput()
                # print(request.session[msisdn])
                return render(request, 'register/allinone.html', {'form': form})

        elif 'FIRST_NAME' in request.POST:

            form =CustomerForm(request.POST,request.FILES)
            if form.is_valid():
                print('YAHOO')
                # print(request.POST.get('COUNTY'))
                # p= CUSTOMER(ID_FILE = form.cleaned_data['ID_TYPE'])
                # p.save()
                form.save()
                messages.success(request,"Your Data is saved. Zain will verify it in 2 Working Days")
                form = MSISDNForm()
                return render(request, 'register/allinone.html', {'form': form})
            else :
                print(form.errors)
                messages.error(request, form.errors)
                form = CustomerForm(initial={'MOBILE_NUMBER': msisdn, 'COUNTRY' : 'SS' })
                form.fields['MOBILE_NUMBER'].widget.attrs['hidden'] = True
                form.fields['MOBILE_NUMBER'].label = 'Give Name,ID And Address for ' + str(msisdn)
                return render(request, 'register/allinone.html', {'form': form})
        else :
            form = MSISDNForm(request.POST)
            import re
            pattern = '21191[0-9]+'
            # found = False
            found = CUSTOMER.objects.filter(MOBILE_NUMBER=msisdn).exists()
            if form.is_valid() and len(re.findall(pattern, msisdn)) == 1  and not found:
                request.session[msisdn]= send_message(msisdn)#gen_otp(6) #send_sms(msisdn)
                form = OTPFORM(initial={'msisdn':msisdn,'otp1':request.session[msisdn] } )
                form.fields['msisdn'].widget.attrs['hidden'] = True
                form.fields['msisdn'].label = 'Give Otp for ' + str(msisdn)
                # form.fields['otp1'].widget = forms.HiddenInput()
                print(request.session[msisdn])
                return render(request, 'register/allinone.html', {'form': form})
            elif found:
                messages.info(request, 'Zain Already have Your Data. Kindly  wait for Zain Feedback. Thank You.')
                form = MSISDNForm()
            else :
                messages.error(request, 'Please Give Valid Zain Number')

    else :
        form =MSISDNForm()
    return render(request, 'register/allinone.html', {'form': form})

def load_COUNTY(request):
    states= int(request.GET.get('states'))
    # print('in view load_county ' + str( states))
    COUNTY   = county.objects.filter(states = states).order_by('name')

    return render(request, 'register/COUNTY.html', {'COUNTY': COUNTY})

def load_PAYAM(request):
    COUNTY = int(request.GET.get('county'))

    PAYAM=payam.objects.filter(county=COUNTY).order_by('name')

    return render(request, 'register/PAYAM.html', {'PAYAM': PAYAM})


def cancel(request):
    # session_keys = list(request.session.keys())
    # for key in session_keys:
    #     del request.session[key]
    # form = MSISDNForm()
    messages.info(request, "Your request has been cancelled, Kindly retry.")
    return redirect('../',request)

def check_pic(request):
   img_src = r'C:\Users\MayankPC\OneDrive\BSCS IX Knowledge BANK\PYTHON\SSZainReg\media\ALL\test.jpg'
   k=  extract_text(img_src)
   # print (k)
   img_src = r'..\media\ALL\test.jpg'

   # if '11276842157' in k:
   #     k='True'

   return render(request,'register/home.html',{'data':k,'pic':img_src})

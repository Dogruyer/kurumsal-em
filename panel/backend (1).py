# ## forms.py
#
# from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.forms.models import ModelForm
# from .models import *
#
#
# class LoginForm(ModelForm):
#     username = forms.CharField(required=True, label="email")
#     password = forms.CharField(widget=forms.PasswordInput, required=True)
#
#     class Meta:
#         model = Araba
#
#
# ## models.py
#
# from django.db import models
#
#
# class Araba(models.Model):
#     marka = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     uretici = models.CharField(max_length=100)
#     yil = models.CharField(max_length=100)
#     lastik = models.IntegerField(max_length=100)
#     beygir = models.CharField(max_length=100)
#     kackapi = models.CharField(max_length=100)
#     eps = models.CharField(max_length=100)
#     abs = models.CharField(max_length=100)
#     havayastigi = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)


# # views.py
# def yeni(request):
#     if request.POST:
#         form = TestFormu(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#
#             return HttpReponse("Kaydedildi")
#
#     form = TestFormu()
#
#     c = {"form": form,
#          "request": request}
#
#     c.update(csrf(request))
#
#     return render(request,"panel/test.html", c)

# ## template
# <form method="POST" action="" class="form-signin" role="form" enctype="multipart/form-data">#}
#        {% for field in form %}
#            <label></label>
#            <input type="{{field.field.widget.input_type}}"
#                    name="{{field.html_name}}"
#                    class="form-control"
#                    placeholder="{{field.label}}" required autofocus>
#            <br>
#         {% endfor %}
#         <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}" />
#         <button class="btn btn-lg btn-primary btn-block" type="submit">Kaydet</button>
#     </form>
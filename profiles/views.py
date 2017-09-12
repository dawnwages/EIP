# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Profile
from .forms import UserForm

from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

@login_required() #only logged in users should access this

def edit_user(request):
	#added to the first line to require the user to be authenticated and keeps the pk out of the url call
	pk = request.user.pk
	#querying the User object with pk from url
	user = User.objects.get(pk=pk)

	#prepopulate UserProfileForm ==> UserForm with retrieved user values from above.
	user_form = UserForm(instance=user)

	#The sorcery begins from here, see explanation below
	ProfileInlineFormset = inlineformset_factory(User, Profile, fields=('FirstName', 'FullName', 'bio', 'location', 'birth_date', 'Dept_Choices',))	
	formset = ProfileInlineFormset(instance=user)

	if request.user.is_authenticated() and request.user.id == user.id:
		if request.method == "POST":
			user_form = UserForm(request.POST, request.FILES, instance=user)
			formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

			if user_form.is_valid():
				created_user = user_form.save(commit=False)
				formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

				if formset.is_valid():
					created_user.save()
					formset.save()
					return HttpResponseRedirect('/accounts/profile/')

		return render(request, "account/account_update.html", {
			"noodle": pk,
			"noodle_form": user_form,
			"formset": formset,
		})
	else:
		raise PermissionDenied

 #Create your views here.
def profile_page(request):
	pk = request.user.pk
	#portfolio = Sku.objects.select_related('article__article_num')
	user = User.objects.get(pk=pk)
	page_profile = Profile.objects.select_related('User')
	user.save()
	#queryset = portfolio.article
  	return render(request, 'profiles/profiles.html', {'user': user})
    

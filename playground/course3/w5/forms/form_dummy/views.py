from django.shortcuts import render
from django.views import View
from django.http import HttpRequest
from .forms import DummyForm


class FormDummyView(View):
	def get(self, request: HttpRequest):
		form = DummyForm()
		#param = request.GET.get('param')
		return render(request, 'form.html', {'form': form})

	def post(self, request: HttpRequest):
		form = DummyForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			context = form.cleaned_data
			return render(request, 'form.html', context)
		else:
			print(request)
			return render(request, 'error.html', {'error': form.errors})
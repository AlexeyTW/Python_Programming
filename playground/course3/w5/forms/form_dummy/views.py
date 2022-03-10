from django.shortcuts import render
from django.views import View
from django.http import HttpRequest


class FormDummyView(View):
	def get(self, request: HttpRequest):
		param = request.GET.get('param')
		return render(request, 'form.html', {'param': param})

	def post(self, request: HttpRequest):
		feedback = request.POST.get('feedback')
		rate = request.POST.get('rate')
		context = {
			'feedback': feedback,
			'rate': rate
		}
		print(feedback, rate)
		return render(request, 'form.html', context)
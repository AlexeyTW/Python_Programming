from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, JsonResponse
from .forms import DummyForm
from .schemas import REVIEW_SCHEMA
from jsonschema.validators import validate
from jsonschema.exceptions import ValidationError
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class FormDummyView(View):
	def get(self, request: HttpRequest):
		form = DummyForm()
		return render(request, 'form.html', {'form': form})

	def post(self, request: HttpRequest):
		form = DummyForm(request.POST)
		if form.is_valid():
			context = form.cleaned_data
			return render(request, 'form.html', context)
		else:
			return render(request, 'error.html', {'error': form.errors})

@method_decorator(csrf_exempt, name='dispatch')
class SchemaView(View):
	def post(self, request: HttpRequest):
		print(request.body)
		try:
			document = json.loads(request.body)
			validate(document, REVIEW_SCHEMA)
			return JsonResponse(document, status=201)
		except json.JSONDecodeError:
			return JsonResponse({'error': 'Incorrect JSON'}, status=400)
		except ValidationError as exc:
			return JsonResponse({'error': exc.message}, status=400)

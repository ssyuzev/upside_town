from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import PersonCreateForm


@method_decorator(csrf_exempt, name='dispatch')
class PersonCreateView(View):

    def post(self, request):
        form = PersonCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True}, status=201)
        else:
            errors = dict(form.errors.items())
            return JsonResponse(
                {"success": False, "errors": f"{errors}"}, status=400
            )


class MatchView(View):
    pass


class ListView(View):
    def get(self, request):
        return JsonResponse({"status": "Ok"})

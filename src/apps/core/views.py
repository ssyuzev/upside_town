from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from .forms import PersonCreateForm, AddLikeForm
from .models import Like
from .mailer import send_email

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


@method_decorator(csrf_exempt, name='dispatch')
class MatchView(View):

    def post(self, request):
        form = AddLikeForm(request.POST)
        if form.is_valid():
            from_ = request.POST["from_person"]
            to_ = request.POST["to_person"]
            if from_ == to_:
                return JsonResponse({"success": False, "errors": "You can't like this person"}, status=400)
            form.save()
            matched = Like.objects.filter(to_person=from_, from_person=to_).first()
            is_match = True if matched else False
            if is_match:
                mail_data = dict(
                    match_email=matched.from_person.email,
                    match_full_name=matched.from_person.full_name,
                    match_gender=matched.from_person.gender,
                    full_name_to=matched.to_person.full_name,
                    mail_to=matched.to_person.email,
                )
                send_email(mail_data)
            return JsonResponse({"match": is_match}, status=201)
        else:
            errors = dict(form.errors.items())
            return JsonResponse(
                {"success": False, "errors": f"{errors}"}, status=400
            )


class ListView(View):
    def get(self, request):
        return JsonResponse({"status": "Ok"})

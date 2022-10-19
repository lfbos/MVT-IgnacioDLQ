from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family.models import Family


def create_family(request, name: str, last_name: str, birthdate: str):

    template = loader.get_template("family/new_member.html")

    new_member = Family(
        name=name, last_name=last_name, birthdate=birthdate
    )
    new_member.save()  

    context_dict = {"new_member": new_member}
    render = template.render(context_dict)
    return HttpResponse(render)


def family(request):
    family = Family.objects.all()

    context_dict = {"family": family}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",)
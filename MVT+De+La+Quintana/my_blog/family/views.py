from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family.models import family


def create_family(request, name: str, last_name: str, BirthDate: str):

    template = loader.get_template("template_family.html")

    family = family(
        name=name, last_name=last_name, BirthDate=BirthDate
    )
    Family.save()  

    context_dict = {"family": family}
    render = template.render(context_dict)
    return HttpResponse(render)


def family(request):
    family = family.objects.all()

    context_dict = {"family": family}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",)
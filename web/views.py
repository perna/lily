from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from icon_manager.models import Icon, IconFile


def index(request):
    return render(request, "web/search_form.html")
    

def search(request):
    term = request.GET["term"]

    result = Icon.objects.filter(
            Q(name__icontains=term) | Q(tags__overlap=[term]) 
        )
        
    context = {"icons": result}

    return render(request, "web/result_search.html", context)


def details(request, slug):
    icon = get_object_or_404(Icon, slug=slug)
    icon_files = icon.files.all()
    thumbnail = icon.files.get(file_extension='SVG')

    context = {
        "icon": icon,
        "thumbnail": thumbnail,
        "files": icon_files
    }

    return render(request, "web/details.html", context)

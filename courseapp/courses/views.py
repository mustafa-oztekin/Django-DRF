from datetime import datetime
from django.shortcuts import get_object_or_404, redirect, render, HttpResponse

from courses.forms import CourseCreateForm, UploadFrom
from .models import Course, Category, Slider, UploadModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
# forms
# GET => url = querystring
# POST

def index(request):
    # list comphension
    # filtrelenmis bir sekilde kurslari sayfaya basar
    # kurslar = [course for course in db["courses"] if course["isActive"]==True]
    kurslar = Course.objects.filter(isActive=1, isHome=True)
    kategoriler = Category.objects.all()
    sliders = Slider.objects.filter(isActive=True)

    return render(request, 'courses/index.html', {
        'categories': kategoriler,
        'courses': kurslar,
        'sliders': sliders
    })




def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        kurslar = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        kategoriler = Category.objects.all()
    else:
        return redirect("/kurslar") 

    return render(request, 'courses/search.html', {
        'categories': kategoriler,
        'courses': kurslar
    })




def upload(request):
    if request.method == "POST":
        form = UploadFrom(request.POST, request.FILES)
        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request, 'courses/success.html')
    else:
        form = UploadFrom()
    return render(request, 'courses/upload.html', {"form":form})



def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            kurs = Course(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                image = form.cleaned_data["image"],
                slug = form.cleaned_data["slug"])
            kurs.save()
            return redirect("/kurslar")
    
    else:
        form = CourseCreateForm()
    return render(request, 'courses/create-course.html', {"form":form})




def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)




def getCoursesByCategory(request, slug):
    kurslar = Course.objects.filter(categories__slug=slug, isActive=True)
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page', 1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {
        'categories': kategoriler,
        'page_obj': page_obj,
        'seciliKategori': slug
    })
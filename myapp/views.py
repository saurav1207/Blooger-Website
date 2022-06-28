from django.shortcuts import render, HttpResponse
from myapp.models import Blog, Contact
import math


# Create your views here.
def home(request):
    # return HttpResponse("this is home")
    return render(request, 'index.html')

def blog(request):
    # return HttpResponse("this is blog")
    no_of_posts = 3
    # if request.GET['pageno']
    page = request.GET.get('page')
    if page is None:
        page = 1
    else:
        page = int(page)
    # print(page)

    '''
    1 : 0 - 4
    2 : 4 - 8
    3 : 8 - 12
    
    1 : 0 - 0 + 
    2 : no_of_post to no_of_post + no_of_post
    3 : no_of_post + no_of_post to no_of_post + no_of_post + no_of_post

    (page_no - 1) * no_of_post to page_no * no_of_post

    '''

    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page - 1) * no_of_posts: page * no_of_posts]

    if page>1:
        prev = page - 1
    else:
        prev = None

    if page<math.ceil(length/no_of_posts):
        nxt = page + 1
    else:
        nxt = None
    
    # ceil funtion
    # 3.67 - 4
    # 5.66 - 6
    
    
    context = {'blogs': blogs, 'prev': prev, 'nxt': nxt}
    return render(request, 'bloghome.html', context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog': blog}
    # return HttpResponse(f"You are viewing {slug}")
    return render(request, 'blogpost.html', context)

def search(request):
    return render(request, 'search.html')

def contact(request):
    # return HttpResponse("this is contact")
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        instance = Contact(name=name, phone=phone, email=email, desc=desc)
        instance.save()
    return render(request, 'contact.html')

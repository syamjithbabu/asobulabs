from django.shortcuts import render
from web.models import Workshop, SubWorkshop, Blog, Team, Contact
from urllib.parse import urlencode, quote
from django.shortcuts import redirect

# Create your views here.

def index(request):
    team = Team.objects.filter().order_by('id')
    blogs = Blog.objects.filter().all()[:2]
    context = {
        'teams' : team,
        'blogs' : blogs
    }
    return render(request,'web/index.html',context)

def contact(request):
    mailto_link = None
    if request.method == 'POST':
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        company = request.POST.get("company")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        
        # Save contact to the database
        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            company=company,
            email=email,
            phone=phone,
            message=message
        )
        contact.save()

        subject = "New Contact Form Submission"
        message_body = (
            f"You have a new contact form submission:\n\n"
            f"Name: {first_name} {last_name if last_name else ''}\n"
            f"Company: {company if company else 'N/A'}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Message: {message}"
        )

        # Encode parameters for the mailto link
        params = urlencode({
            'subject': subject,
            'body': message_body
        })
        mailto_link = f"mailto:contact@asobulabs.com?{params}"
        print(mailto_link)  # Debug: Check the generated link

    return render(request, 'web/contact.html', {'mailto_link': mailto_link})


def about(request):
    team = Team.objects.filter().order_by('id')
    context = {
        'teams' : team
    }
    return render(request,'web/about.html',context)

def consulting(request):
    return render(request,'web/consulting.html')

def learning(request):
    workshops = Workshop.objects.filter().order_by('id')
    context = {
        'workshops' : workshops
    }
    return render(request,'web/learning.html',context)

def our_works(request):
    return render(request,'web/works.html')

def blogs(request):
    blogs = Blog.objects.filter()[:6]
    context = {
        'blogs' : blogs
    }
    return render(request,'web/blogs.html',context)

def blog_details(request,blog_slug):
    print(blog_slug)
    blog = Blog.objects.get(slug=blog_slug)
    print(blog.blog_title)
    context = {
        'blog' : blog
    }
    return render(request,'web/blog-details.html',context)

def lego(request):
    return render(request,'web/lego.html')

def design_thinking(request):
    return render(request,'web/design-thinking.html')

def future_thinking(request):
    return render(request,'web/future-thinking.html')

def workshop_details(request,workshop_slug):
    print(workshop_slug)
    workshop = Workshop.objects.get(slug=workshop_slug)
    sub_workshops = SubWorkshop.objects.filter(workshop=workshop)
    try:
        next_workshop = Workshop.objects.filter(id__gt=workshop.id).order_by('id').first()
    except Workshop.DoesNotExist:
        next_workshop = None
    try:
        previous_workshop = Workshop.objects.filter(id__lt=workshop.id).order_by('-id').first()
    except Workshop.DoesNotExist:
        previous_workshop = None
    context = {
        'workshop' : workshop,
        'sub_workshops' : sub_workshops,
        'next_workshop': next_workshop,
        'previous_workshop': previous_workshop
    }
    return render(request, 'web/workshop-details.html',context)

def service_design(request):
    return render(request, 'web/service-design.html')

def business_advisory(request):
    return render(request,'web/business-advisory.html')

def new_venture_development(request):
    return render(request,'web/new-venture-development.html')
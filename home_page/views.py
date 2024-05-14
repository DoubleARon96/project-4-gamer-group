from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import HomePage






class HomePage_View (generic.ListView) :
    queryset = HomePage.objects.all()
    template_name = "home_page.html"
    paginate_by = 1

        

    def HomePageLoader(request, slug):
            # Retrieve the specific HomePage instance based on the slug
            queryset = HomePage.objects.filter()
            slug = get_object_or_404(HomePage, slug=slug)

            title = HomePage.title
            content = HomePage.content.all()
            gamer_tag = HomePage.gamer_tag

            
            comments = post.comments.all().order_by("-created_on")
            comment_count = post.comments.filter(approved=True).count()

            return render(request, 'home_page.html', {
                "title": title,
                "content": content,
                "gamer_tag": gamer_tag,
            })

def HomePageLoader(request):
    
    return render(request, 'home_page.html')
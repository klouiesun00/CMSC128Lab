from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import review_post
from .forms import ReviewPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class BookReviewsView(ListView):
    model = review_post
    template_name = 'pages/book-reviews.html'

@login_required
def CreatePostView(request):
    post_form = ReviewPostForm()
    if request.method == "POST":
        post_form = ReviewPostForm(request.POST)
        if post_form.is_valid():
            review_post.objects.create(**post_form.cleaned_data)
            post_form = ReviewPostForm()
    context = {
        "form": post_form
    }
    return render(request, "posts/make-a-post.html", context)
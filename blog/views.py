from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models
from .forms import CommentForm
from mainpage.models import Detail

# Create your views here.
def blog_single(request, blog_id):
    blog = get_object_or_404(models.BlogPage, pk=blog_id)
    comments = blog.comments.filter(active=True)
    total_comments = len(comments)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = blog
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/blog-single.html', {'blog': blog,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'comment_total': total_comments})

def all_blogs(request):
    blogp = models.BlogPage.objects.order_by('-pub_date')
    infor = Detail.objects.first()
    return render(request, 'blog/allblogs.html', {'blog': blogp,
    'infor': infor,})
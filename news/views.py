from django.http.response import  Http404
from django.shortcuts import render_to_response, redirect
from news.models import News, Comments
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf
from news.forms import CommentForm
from django.contrib import auth

def news(request):
    return render_to_response('news/news.html',{'news': News.objects.all(), 'username': auth.get_user(request).username,
                                                'id':auth.get_user(request).id})

def new(request, news_id = 1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['news'] = News.objects.get(id = news_id)
    args['comments'] = Comments.objects.filter(comments_news_id = news_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('new.html', args)

def addlike(request, news_id):
    try:
        news = News.objects.get(id = news_id)
        news.news_likes += 1
        news.save();
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, news_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.comments_news = News.objects.get(id = news_id)
            form.save()
    return redirect('/news/get/%s/' % news_id)

from django.shortcuts import render,HttpResponse,redirect
from .models import Post,blogComment
from django.contrib import messages
from blog.templatetags import extras

# Create your views here.
def bloghome(request):
    allPost = Post.objects.all()
    # print(allPost)
    context = {'allpost':allPost}

    return render(request,'blog/bloghome.html',context)

def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    comments= blogComment.objects.filter(post=post, parent=None)
    replies= blogComment.objects.filter(post=post).exclude(parent=None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments, 'user': request.user, 'replyDict': replyDict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')

        if comment=="":
            messages.warning(request, "Please enter the comment....!")


        elif parentSno=='':
            comment=blogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")

        else:
            parent = blogComment.objects.get(sno = parentSno)
            comment=blogComment(comment= comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, "Your replay has been posted successfully")

        
    return redirect(f"/blog/{post.slug}")

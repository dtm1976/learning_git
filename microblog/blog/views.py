from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView
# from django.http import HttpResponse
from .models import Post
from .forms import PostForm, PostModelForm


# Create your views here.
def index(request):
    # name = "Main Accademy"
    # return HttpResponse(f"<h1>Hello, world!</h1>  <h2>Congratulation {name}</h2>")
    return render(request, 'blog/base_blog.html')


def posts_list(request):
    posts = Post.objects.all().order_by('-publish')
    return render(request, 'blog/posts_list.html', context={'posts': posts})


# def post_create(request):
#     if request.method == 'POST':
#         post = Post.objects.create(title=request.POST['title'],
#                                    slug=request.POST['slug'],
#                                    body=request.POST['body'])
#         return render(request, 'blog/post_detail.html', context={'post': post})
#     return render(request, 'blog/post_create.html')


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create.html', context={'form': form})

    def post(self, request):
        # new_post = Post.objects.create(title=request.POST['title'],
        #                            slug=request.POST['slug'],
        #                            body=request.POST['body'])
        bound_form = PostModelForm(request.POST)
        # bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)  # render(request, 'blog/post_detail.html', context={'post': new_post})
        return render(request, 'blog/post_create.html', context={'form': bound_form})

# def post_detail(request, slug):
#     post = Post.objects.get(slug__iexact=slug)
#     return render(request, 'blog/post_detail.html', context={'post': post})


class PostDetail(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


class PostUpdate(View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        # bound_form = PostModelForm(instance=post)
        bound_form = PostForm({'title': post.title, 'slug': post.slug, 'body': post.body})
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        # update_post = Post(title=request.POST['title'],
        #                                      slug=request.POST['slug'],
        #                                      body=request.POST['body'])
        # post.title, post.slug, post.body = update_post.title, update_post.slug, update_post.body
        # post.save()
        bound_form = PostModelForm(request.POST, instance=post)
        # bound_form = PostForm({'title': request.POST['title'],
        #                        'slug': request.POST['slug'],
        #                        'body': request.POST['body'],
        #                        })
        if bound_form.is_valid():
            new_post = bound_form.save()
            # new_post = bound_form.save(old_values=post)
            return redirect(new_post)
        return render(request, 'blog/post_update.html', context={'form': bound_form, 'post': post})


class PostDelete(View):

    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostModelForm(instance=post)  # instance=post
        # bound_form = PostForm({'title': post.title, 'slug': post.slug, 'body': post.body})
        return render(request, 'blog/post_delete.html', context={'form': bound_form, 'post': post})

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


class PostListView(ListView):
    queryset = Post.objects.all().order_by('-publish')
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/posts_list.html'

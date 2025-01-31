from django.shortcuts import render
from django.views.generic import ListView
from .models import Post
from .forms import CommentForm # new
from django.views import View

from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse


class CommentGet(DetailView):
    """
    View to display a single post with a comment form.

    Extends Django's DetailView to display a single post and a comment form.
    """
    model = Post
    template_name = "post_detail.html"

    def get_context_data(self, **kwargs):
        """
        Add a blank comment form to the context.

        Calls the parent get_context_data method and adds a blank CommentForm
        to the context.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()

        return context
    
class CommentPost(SingleObjectMixin, FormView): # new
    """
    View to handle a form post request to create a new comment.

    Extends Django's SingleObjectMixin and FormView to handle a form post
    request to create a new comment and associate it with the post.
    """
    model = Post
    form_class = CommentForm
    template_name = "post_detail.html"

    def post(self, request, *args, **kwargs):
        """
        Handle a form post request to create a new comment.

        Calls the parent post method to create a new comment and associate it
        with the post.
        """
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        """
        Set the comment's author to the current user and save the comment.

        Calls the parent form_valid method to create a new comment and sets
        the comment's author to the current user before saving the form.
        """
        comment = form.save(commit=False)
        comment.article = self.object
        comment.author = self.request.user
        comment.save()

        return super().form_valid(form)
    
    
    def get_success_url(self):
        """
        Redirect to the book detail page after creating a new comment.

        Returns the URL to redirect to after creating a new comment, which is
        the book detail page.
        """
        post = self.get_object()
        return reverse('catalog:book_detail', kwargs={'pk': post.book.id})
class PostDetailView(LoginRequiredMixin, View):

    def get_context_data(self, **kwargs):
        """
        Add a blank comment form to the context.

        Calls the parent get_context_data method and adds a blank CommentForm
        to the context.
        """
        context = super().get_context_data(**kwargs)
        context['form']  = CommentForm
        return context
    
    def get(self, request, *args, **kwargs):
        """
        Handle a GET request to display a single post with a comment form.

        Calls the CommentGet view to display a single post and a comment form.
        """
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        Handle a form post request to create a new comment.

        Calls the CommentPost view to handle a form post request to create a
        new comment and associate it with the post.
        """
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """
    View to update a single post.

    Extends Django's UpdateView to update a single post.
    """
    model = Post
    fields = (
        "title",
        "body",
    )

    template_name = "post_edit.html"
    def get_success_url(self):
        return reverse_lazy('catalog:book_detail', kwargs={'book_id': self.kwargs['book_id']})

class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete a single post.

    Extends Django's DeleteView to delete a single post.
    """
    model = Post
    template_name = "post_delete.html"

    def get_success_url(self):
        return reverse_lazy('catalog:book_detail', kwargs={'book_id': self.kwargs['book_id']})

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    View to handle creating a new post.

    Creates a new post from the title and body form fields. Uses the
    CreateView generic view and defines a form_valid method to set
    the post's author to the current user before saving the form.
    """
    model = Post
    template_name = "post_form.html"

    fields = (
        "title",
        "body",
    )

    def form_valid(self, form):
        """
        Set the post's author to the current user before saving the form.

        Calls the parent form_valid method after setting the post's author
        to the current user.
        """
        form.instance.author = self.request.user
        form.instance.book_id = self.kwargs['book_id']
        
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('catalog:book_detail', kwargs={'book_id': self.kwargs['book_id']})



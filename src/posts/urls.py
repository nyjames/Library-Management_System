from django.urls import path

from .views import(

    PostDetailView, # new
   PostUpdateView, # new
    PostDeleteView, # new
   PostCreateView, # new
)

# URL pattern to display the detail of a single post for a specific book.
# The URL takes two int parameters (book_pk, pk) which are the primary keys of the book and the post.
# The view class is PostDetailView.
# The name of the URL pattern is 'post_detail'.
urlpatterns = [
    path("<int:book_id>/<int:pk>/", PostDetailView.as_view(),
        name="post_detail"), # new
    # URL pattern to edit an existing post.
    # The URL takes an int parameter (pk) which is the primary key of the post.
    # The view class is PostUpdateView.
    # The name of the URL pattern is 'post_edit'.
    path("<int:book_id>/<int:pk>/edit/", PostUpdateView.as_view(),
        name='post_edit'), # new
    # URL pattern to delete an existing post.
    # The URL takes an int parameter (pk) which is the primary key of the post.
    # The view class is PostDeleteView.
    # The name of the URL pattern is 'post_delete'.
    path("<int:book_id>/<int:pk>/delete/", PostDeleteView.as_view(),
        name='post_delete'), # new
    # URL pattern to create a new post.
    # The view class is PostCreateView.
    # The name of the URL pattern is 'post_new'.
    path('<int:book_id>/new/', PostCreateView.as_view(),
         name='post_form'), # new

]

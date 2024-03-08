# Imports
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.db.models import Count, Q
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from items.models import Category, Item, ItemComments
from items.forms import ItemCommentForm


class ShopView(generic.ListView):
    """
    Class generates view of items page
    """

    template_name = "items/shop.html"

    def get(self, request, category_pk, *args, **kwargs):
        """This method generates view of items page"""
        all_categories = Category.objects.all().order_by('category_name')
        page_sort = int(request.GET.get('page_sort', 0))
        page_length = int(request.GET.get('page_length', 8))
        current_page = request.GET.get('page', 1)
        if category_pk == 0:
            queryset = Item.objects.all().order_by('item_name').annotate(
            item_comments_num=Count(
                "item_comments", filter=Q(item_comments__approved=1)
            )
        )
            selected_category = 'All Products'
        else:
            queryset = Item.objects.filter(item_category__pk=category_pk).annotate(
            item_comments_num=Count(
                "item_comments", filter=Q(item_comments__approved=1)
            )
        )
            running_category = Category.objects.filter(pk=category_pk).first()
            selected_category = running_category.category_name
        if page_length != 0:
            if page_sort == 5:
                paginated_items = Paginator(queryset.order_by('item_likes_num'), page_length)
            elif page_sort == 4:
                paginated_items = Paginator(queryset.order_by('-item_likes_num'), page_length)
            elif page_sort == 3:
                paginated_items = Paginator(queryset.order_by('-price_per_unit'), page_length)
            elif page_sort == 2:
                paginated_items = Paginator(queryset.order_by('price_per_unit'), page_length)
            elif page_sort == 1:
                paginated_items = Paginator(queryset.order_by('-item_name'), page_length)
            elif page_sort == 0:
                paginated_items = Paginator(queryset.order_by('item_name'), page_length)
            else:
                paginated_items = Paginator(Item.objects.all(), 10)
            page_obj = paginated_items.get_page(current_page)
            paginator_nav = True
        else:
            if page_sort == 5:
                page_obj = queryset.order_by('item_likes_num')
            elif page_sort == 4:
                page_obj = queryset.order_by('-item_likes_num')
            elif page_sort == 3:
                page_obj = queryset.order_by('-price_per_unit')
            elif page_sort == 2:
                page_obj = queryset.order_by('price_per_unit')
            elif page_sort == 1:
                page_obj = queryset.order_by('-item_name')
            elif page_sort == 0:
                page_obj = queryset.order_by('item_name')
            else:
                page_obj = Item.objects.all()
            paginator_nav = False
        # Render template
        return render(
            request,
            self.template_name,
            {
                "all_categories": all_categories,
                "items": page_obj,
                "selected_category": selected_category,
                "paginator_nav": paginator_nav,
                "page_sort": page_sort,
                "page_length":page_length,
            },
        )
        
        
class ItemDetailView(generic.ListView):
    """
    Class generates view of item's detail
    """

    template_name = "items/item_detail.html"
    
    def get(self, request, item_pk, *args, **kwargs):
        liked = False
        disliked = False
        item_comment_form = ItemCommentForm()
        item_to_view = get_object_or_404(Item.objects.annotate(
            item_comments_num=Count("item_comments", filter=Q(item_comments__approved=1))
            ), pk=item_pk)
        comments = (
            ItemComments.objects.filter(item__in=[item_to_view])
            .filter(approved=1)
            .order_by("-created_on")
        )
        if request.user.is_authenticated:
            users_wishlist = request.user.userprofile.user_wishlist
            if item_to_view.item_sku in users_wishlist:
                in_wishlist = True
            else:
                in_wishlist = False
        else:
            in_wishlist = False
        if item_to_view.item_likes.filter(id=self.request.user.id).exists():
            liked = True
        if item_to_view.item_dislikes.filter(id=self.request.user.id).exists():
            disliked = True
        # Render template
        return render(
            request,
            self.template_name,
            {
                "item": item_to_view,
                "comments": comments,
                "can_comment": True,
                "item_comment_form": item_comment_form,
                "in_wishlist": in_wishlist,
                "liked": liked,
                "disliked": disliked,
            },
        )

    def submit_comment(request, item_pk, *args, **kwargs):
        """
        Function is called when comment submitted
        """
        item_to_view = get_object_or_404(Item.objects.annotate(
            item_comments_num=Count("item_comments", filter=Q(item_comments__approved=1))
            ), pk=item_pk)
        comments = (
            ItemComments.objects.filter(item__in=[item_to_view])
            .filter(approved=1)
            .order_by("-created_on")
        )
        # Get comment from form
        item_comment_form = ItemCommentForm(data=request.POST)
        # If form valid save comment
        if item_comment_form.is_valid():
            item_comment_form.instance.comment_author = request.user
            new_comment = item_comment_form.save(commit=False)
            new_comment.item = item_to_view
            new_comment.save()
            messages.success(request, f'Your comment regarding {item_to_view} was submitted and pending approval.')
        # If not valid, return form
        else:
            item_comment_form = ItemCommentForm()
        return render(  # Render template
            request,
            'items/item_detail.html',
            {
                "item": item_to_view,
                "comments": comments,
                "can_comment": False,
                "item_comment_form": item_comment_form,
            }
        )
    
    
class ItemLikeView(LoginRequiredMixin, generic.ListView):

    def get(self, request, item_pk, *args, **kwargs):
        selected_item = get_object_or_404(Item, pk=item_pk)
        if not selected_item.item_likes.filter(id=request.user.id).exists():
            selected_item.item_likes.add(request.user)
            if selected_item.item_dislikes.filter(id=request.user.id).exists():
                selected_item.item_dislikes.remove(request.user)
            messages.success(request, f"You like {selected_item.item_name} :)")
        else:
            selected_item.item_likes.remove(request.user)
            messages.success(request, f"You don't like {selected_item.item_name} anymore :(")
        return redirect('item-detail', item_pk=item_pk)
    

class ItemDislikeView(LoginRequiredMixin, generic.ListView):

    def get(self, request, item_pk, *args, **kwargs):
        selected_item = get_object_or_404(Item, pk=item_pk)
        if not selected_item.item_dislikes.filter(id=request.user.id).exists():
            selected_item.item_dislikes.add(request.user)
            if selected_item.item_likes.filter(id=request.user.id).exists():
                selected_item.item_likes.remove(request.user)
            messages.success(request, f"You dislike {selected_item.item_name} :(")
        else:
            selected_item.item_dislikes.remove(request.user)
            messages.success(request, f"You don't dislike {selected_item.item_name} anymore :)")
        return redirect('item-detail', item_pk=item_pk)
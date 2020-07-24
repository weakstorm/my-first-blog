from django.urls import reverse_lazy
from django.views import generic
from .forms import ReviewCreateForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Review

# Create your views here.
class ReviewCreate(generic.CreateView):
  model = Review
  form_class = ReviewCreateForm
  success_url = reverse_lazy('reviews:review_list')

# 口コミ一覧
class ReviewDetail(generic.DetailView):
  model = Review

class ReviewList(generic.ListView):
  model = Review
  ordering = '-created_at'

# 口コミ削除
class ReviewDelete(generic.DeleteView):
  model = Review
  success_url = reverse_lazy('reviews:review_list')

# 口コミ更新
class ReviewUpdate(generic.UpdateView):
  model = Review
  form_class = ReviewCreateForm
  success_url = reverse_lazy('reviews:review_list')

# 関数
# 口コミ削除
# def review_delete(request, pk):
#   review = get_object_or_404(Review, pk=pk)
#   if request.method == 'POST':
#     review.delete()
#     return redirect('reviews:review_list')

#   context = {
#     'review': review
#   }
# return render(request, 'reviews/review_confirm_delete.html', context)  
# 口コミ更新
# def review_update(request, pk):
#   review = get_object_or_404(Review, pk=pk)
#   form = ReviewCreateForm(request.POST or None, instance=review)
#   if request.method == 'POST' and form.is_valid():
#     form.save()
#     return redirect('reviews:review_list')

#   context = {
#     'form': form,
#   }
#   return render(request, 'reviews/review_form.html', context)  

# 口コミ作成
# def review_create(request):
#   form = ReviewCreateForm(request.POST or None)
#   if request.method == 'POST' and form.is_valid():
#     form.save()
#     return redirect('reviews:review_list')

#   context = {
#     'form': form,
#   }
#   return render(request, 'reviews/review_form.html', context)

# def review_create_send(request):
#   form = ReviewCreateForm(request.POST)
#   form.save()
#   return redirect('reviews:review_list')

# 口コミ一覧ページ
# def review_detail(request, pk):
#   context = {
#     'review': get_object_or_404(Review, pk=pk),
#   }
#   return render(request, 'reviews/review_detail.html', context)

# def review_list(request):
#   context = {
#     'review_list': Review.objects.all().order_by('-created_at'),
#   }
#   return render(request, 'reviews/review_list.html', context)
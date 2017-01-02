from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from main.models import Rating
from main.models import Item
from django.db.models import Avg
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
import json
import time
import graphlab

def get_movie_info(ids):
    ret = []
    for id in ids:
        item = Item.objects.get(id=id)
        if item.img_src == '':
            item.img_src = 'http://placehold.it/200x300'
        item.genres = []
        for k, v in item.__dict__.items():
            if k.startswith('genre_') and v is True:
                item.genres.append(k[len('genre_'):])
        item_dict = item.__dict__
        del item_dict['_state']
        ret.append(item_dict)
    return ret

def get_history_movie_id_score(request):
    user = request.user.id
    ratings = Rating.objects.filter(user=user)
    ids = [rating.item.id for rating in ratings]
    scores = [rating.rating for rating in ratings]
    return ids, scores

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['auth'] = int(self.request.user.is_authenticated())

        return context


class RatingView(View):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            item = data['item']
            rating = data['rating']
            ts = int(time.time())

            rating_record = Rating(
                user=request.user.id,
                item=Item.objects.get(id=item),
                rating=rating,
                timestamp=ts
            )
            rating_record.save()
        except:
            return HttpResponse(status=500)
        return HttpResponse(status=200)


class HistoryListView(View):
    def get(self, request, *args, **kwargs):
        ids, scores = get_history_movie_id_score(request)
        items = get_movie_info(ids)
        for item, score in zip(items, scores):
            item['rating'] = score

        return JsonResponse({'items': items})


class MovieListView(View):
    def get(self, request, *args, **kwargs):
#        import pdb
#        pdb.set_trace()
        cnt = request.GET.get('count', 20)
        all_items = [item.id for item in Item.objects.all()]
        excluded_items, _ = get_history_movie_id_score(request)
        def _get_recommened_movie_ids():
            if not request.user.is_authenticated():
                avg_scores =  Rating.objects. \
                    exclude(item__in=excluded_items).values('item'). \
                    annotate(average_rating=Avg('rating'))
                top_items = avg_scores. \
                    order_by('-average_rating', 'item')[:cnt]
                return [item['item'] for item in top_items]
            else:
                cf_model = graphlab.load_model('cf_model')
                recomm = cf_model.recommend(
                    users=[request.user.id],
                    k=int(cnt),
                    items=list(set(all_items) - set(excluded_items))
                )
                return recomm['item']

        ids = _get_recommened_movie_ids()
        items = get_movie_info(ids)


        return JsonResponse({'items': items})

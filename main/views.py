from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View
from main.models import Rating
from main.models import Item
from django.db.models import Avg
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        pass



class MovieListView(View):
    def get(self, request, *args, **kwargs):
#        import pdb
#        pdb.set_trace()
        cnt = request.GET.get('count', 10)
        def _get_recommened_movie_ids():
            avg_scores =  Rating.objects.values('item'). \
                          annotate(average_rating=Avg('rating'))
            top_items = avg_scores.order_by('-average_rating')[:cnt]
            return [item['item'] for item in top_items]

        def _get_movie_info(ids):
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




        ids = _get_recommened_movie_ids()
        items = _get_movie_info(ids)


        return JsonResponse({'items': items})


        #if request.user.is_authenticated():



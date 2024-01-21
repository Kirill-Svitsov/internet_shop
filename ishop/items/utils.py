from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q

from items.models import Item


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Item.objects.filter(id=int(query))
    # return Item.objects.annotate(search=SearchVector('name', 'description')).filter(search=query)
    # return Item.objects.filter(description__search=query)
    # keywords = [word for word in query.split() if len(word) > 2]
    # q_objects = Q()
    # for token in keywords:
    #     q_objects |= Q(description__icontains=token)
    #     q_objects |= Q(name__icontains=token)
    # return Item.objects.filter(q_objects)
    vector = SearchVector('name', 'description')
    query = SearchQuery(query)
    result = Item.objects.annotate(
        rank=SearchRank(vector, query)
    ).filter(rank__gt=0).order_by('rank')
    result = result.annotate(
        headline=SearchHeadline(
            'name',
            query,
            start_sel='<span style="background-color: #f8af2e;">',
            stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
            'description',
            query,
            start_sel='<span style="background-color: #f8af2e;">',
            stop_sel="</span>",
        )
    )
    return result

from isarps.models import Isarp

def get_isarps(request):

    isarps = Isarp.objects.filter(public_isarp=True).order_by('order_isarp').values_list('id', 'title_isarp', 'slug_isarp', 'chapters')

    return {
        'isarps': isarps
    }
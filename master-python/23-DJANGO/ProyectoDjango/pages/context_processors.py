from pages.models import Pages

def get_pages(request):
    
    pages = Pages.objects.filter(visible=True).order_by('order').values_list('id','title','slug') #Para que no sea pesado para el frameword se utiliza como recomendacion el value_list() en vez del all()
    
    # flat = True Pasa un texto plano
    
    return {
        'pages':pages
    }
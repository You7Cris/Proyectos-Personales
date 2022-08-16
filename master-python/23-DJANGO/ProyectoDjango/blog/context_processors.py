from blog.models import Category, Article

def get_categories(request):
    
    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True) # Conseguir los ids para la entradas
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id','name') #Para que no sea pesado para el frameword se utiliza como recomendacion el value_list() en vez del all()
    
    # flat = True Pasa un texto plano
    
    return {
        'categories': categories,
        'ids': categories_in_use
    }
from store.models import Category

def category(request):
    category = Category.objects.all();
    return{'categories':category}
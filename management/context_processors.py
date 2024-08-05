from .models import MainInfo, Items

def mainInfo(request):
    return {
        'mainInfo':MainInfo.objects.all()
    }

def menuItems(request):
    return{
        'menuItems': Items.objects.all()
    }
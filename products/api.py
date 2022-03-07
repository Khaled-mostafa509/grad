from .models import Products , Category
from .serializers import ProductsSerializers , CategorySerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET','Post'])

def Products_listAPI(request):
    all_ads=Products.objects.all()
    return Response(ProductsSerializers(all_ads,many=True).data)

@api_view(['GET','POST'])
def Category_list(request):
    all_category= Category.objects.all()
    return Response(CategorySerializers(all_category,many=True).data)
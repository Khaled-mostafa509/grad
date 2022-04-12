from .models import Products , Category
from .serializers import ProductsSerializers , CategorySerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .contentbased import tst
import psycopg2

db = psycopg2.connect(database = 'd6qclb8qlneusj',
                      user = 'gisyouirutkrjn',
                      password = '413f7d63ee654e0f7ed6e6cd014061b47405fb752de9d116d03c6e7ac4bfbb9c',
                      host = 'ec2-54-204-28-187.compute-1.amazonaws.com',
                      port = '5432')

cr = db.cursor()
t = tuple(tst)
cr.execute(f'''UPDATE products_products SET recommended_name={t} WHERE id = 6;''')
db.commit()

@api_view(['GET','Post'])

def Products_listAPI(request):
    all_ads=Products.objects.all()
    return Response(ProductsSerializers(all_ads,many=True).data)

@api_view(['GET','POST'])
def Category_list(request):
    all_category= Category.objects.all()
    return Response(CategorySerializers(all_category,many=True).data)
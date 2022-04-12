from .models import Recommended
from .serializers import RecommendedSerializers
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

cr.execute('''INSERT INTO recommended_recommended(recommended_name) VALUES('7mada');''')
db.commit()





@api_view(['GET'])

def Recommended_listAPI(request):
    all_ads=Recommended.objects.all()
    return Response(RecommendedSerializers(all_ads,many=True).data)
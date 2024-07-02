from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """test Api view """
    
    def get(self,request,format=None):
        """returns a list of apiview features"""
        an_apiview=[ 'uses http methods as function (get,post,patch,put,delete)',
                    'is simillar to a traditional django view',
                    'kally the great!!!']
        
        return Response({'message':"hello",
                         "an_apiview":an_apiview})
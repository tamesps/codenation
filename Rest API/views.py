from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def lambda_function(request):
   if request.method == 'POST':
       received = request.data
       question = received['question']
       response = sorted(question, key=lambda x: (-question.count(x), question.index(x)))
       data = {}
       data['solution'] = response
       return Response(data, status=status.HTTP_200_OK)

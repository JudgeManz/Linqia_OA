from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse

class Vocabulary(APIView):
    vocab = [
            "#ad",
            "#sponsored",
            "advertisement"
        ]
    
    def get(self, request):
        response = {"vocab" : self.vocab}

        return JsonResponse(response)
    
    def post(self, request):
        body = request.data.get("vocab")
        for word in body:
            self.vocab.append(word)
        
        response = {"vocab" : self.vocab}

        return JsonResponse(response)

class Prediction(APIView):
    def post(self, request):
        post_text = request.data.get("post_text").split()
        prediction = "non-sponsored"

        for word in post_text:
            
            if word in Vocabulary.vocab:
                prediction = "sponsored"
                break
        
        response = {"prediction" : prediction}
        
        return JsonResponse(response)
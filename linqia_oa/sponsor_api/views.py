from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse
from .models import Keywords

class Vocabulary(APIView):
    def getVocab(self):
        keywords = Keywords.objects.all()
        vocab = []
        for word in keywords:
            vocab.append(word.keyword)

        return vocab
    
    def get(self, request):
        response = {"vocab" : self.getVocab()}

        return JsonResponse(response)
    
    def post(self, request):
        body = request.data.get("vocab")
        for word in body:
            w = Keywords(keyword=word)
            w.save()

        response = {"vocab" : self.getVocab()}

        return JsonResponse(response)

class Prediction(APIView):
    def post(self, request):
        post_text = request.data.get("post_text").split()
        prediction = "non-sponsored"
        vocab = Vocabulary.getVocab(Vocabulary)

        for word in post_text:
            if word in vocab:
                prediction = "sponsored"
                break
        
        response = {"prediction" : prediction}
        
        return JsonResponse(response)
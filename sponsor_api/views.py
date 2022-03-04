from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Keywords

class Vocabulary(APIView):
    def getVocab(self):
        ''' 
        getVocab is used to get all the sponsorship keywords from the DB
        '''
        
        keywords = Keywords.objects.all()
        vocab = []
        for word in keywords:
            vocab.append(word.keyword)

        return vocab
    
    def get(self, request):
        ''' 
        (GET) Vocabulary: Returns the list of keywords to determine if a test is sponsored
        '''
        response = {"vocab" : self.getVocab()}

        return JsonResponse(response)
    
    def post(self, request):
        ''' 
        (POST) Vocabulary: Add a new keyword to the existing vocabulary then return the complete list of keywords
        '''
        body = request.data.get("vocab")
        for word in body:
            w = Keywords(keyword=word)
            w.save()

        response = {"vocab" : self.getVocab()}

        return JsonResponse(response)

class Prediction(APIView):
    def post(self, request):
        '''
        (POST) Prediction: Predicts if the given post_text is sponsored or not by checking for the keywords in the text
        '''
        
        post_text = request.data.get("post_text").split()
        prediction = "non-sponsored"
        vocab = Vocabulary.getVocab(Vocabulary)

        for word in post_text:
            if word in vocab:
                prediction = "sponsored"
                break
        
        response = {"prediction" : prediction}
        
        return JsonResponse(response)
from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import MultipleObjectsReturned
from django.urls import reverse
from .models import Visit

class VisitCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
       
        page_visited = request.path


        if page_visited.startswith(reverse('admin:index')):
            return None 

        try:
        
            visit = Visit.objects.get(page_visited=page_visited)
        except Visit.DoesNotExist:
      
            visit = Visit.objects.create(page_visited=page_visited, visit_count=1)
        except MultipleObjectsReturned:
      
            visit = Visit.objects.filter(page_visited=page_visited).first()


        visit.visit_count += 1
        visit.save()

        return None

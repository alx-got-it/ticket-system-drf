from django.db import transaction

from rest_framework import viewsets
from rest_framework.exceptions import APIException

from app_core.models import Ticket
from app_core.serializers import TicketSerializer
from app_core.tasks import task_execute


class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                # save instance
                instance = serializer.save()
                instance.save()
                
                # create task params
                job_params = {"db_id": instance.id}
                
                # submit task for background execution
                transaction.on_commit(lambda: task_execute.delay(job_params))
        
        except Exception as e:
            raise APIException(str(e))

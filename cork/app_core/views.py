from django.db import transaction
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from app_core.permissions import IsOwnerOrReadOnly, IsOwner

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets, mixins, permissions
from rest_framework.decorators import action
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, \
    get_object_or_404, GenericAPIView
from rest_framework.response import Response

from app_core.models import Ticket, Location
from app_core.serializers import TicketSerializer
# from app_core.serializers import TicketListSerializer, TicketDetailSerializer, LocationSerializer, \
#     TicketByLocationSerializer, TicketCreateSerializer
from app_core.tasks import task_execute


# class TicketListView(APIView):
#     """ Список объявлений """
#
#     def get(self, request):
#         tickets = Ticket.objects.filter(rejected=False)
#         serializer = TicketListSerializer(tickets, many=True)
#         return Response(serializer.data)
#
#
# class TicketDetailView(APIView):
#     """ Объявление """
#
#     def get(self, request, pk):
#         ticket = Ticket.objects.get(id=pk, rejected=False)
#         serializer = TicketDetailSerializer(ticket)
#         return Response(serializer.data)
#
#
# class TicketCreateView(APIView):
#     """ Создание объявления """
#     def post(self, request):
#         ticket = TicketCreateSerializer(data=request.data)
#         code: int
#         if ticket.is_valid():
#             ticket.save()
#             code = 201
#         else:
#             code = 400
#         return Response(status=code)


# class TicketByLocationView(APIView):
#     """ Список объявлений по локации """
#
#     def get(self, request, slug):
#         location = Location.objects.get(slug=slug)
#         tickets = Ticket.objects.filter(location=location.id, rejected=False)
#         serializer = TicketByLocationSerializer(tickets, many=True)
#         return Response(serializer.data)


# Запуск Тасок при вызове Вьюхи
#
# class TicketViewSet(viewsets.ModelViewSet):
#     serializer_class = TicketSerializer
#     queryset = Ticket.objects.all()
#
#     def perform_create(self, serializer):
#         try:
#             with transaction.atomic():
#                 # save instance
#                 instance = serializer.save()
#                 instance.save()
#
#                 # create task params
#                 job_params = {"db_id": instance.id}
#
#                 # submit task for background execution
#                 transaction.on_commit(lambda: task_execute.delay(job_params))
#
#         except Exception as e:
#             raise APIException(str(e))


# class TicketsByLocationView(ListAPIView):
#     serializer_class = TicketsByLocationSerializer
#
#     def get_queryset(self):
#         location = self.kwargs['location']
#         return Ticket.objects.filter(location=location)
#
#
# class LocationViewSet(mixins.RetrieveModelMixin,
#                       mixins.ListModelMixin,
#                       viewsets.GenericViewSet):
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#
#
# class ByLocationViewSet(mixins.RetrieveModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     serializer_class = TicketSerializer
#
#     def get_queryset(self):
#         location = self.kwargs['location']
#         return Ticket.objects.filter(location=location)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# TODO: HERE *
# class ComputerViewSet(viewsets.ModelViewSet):
#     queryset = Computer.objects.all()
#     serializer_class = ComputerSerializer
#     lookup_value_regex = r"(?P<org_slug>[^/.]+)/(?P<slug>[-\w]+)"
#
#     def get_object(self):
#         queryset = self.filter_queryset(self.get_queryset())
#         obj = get_object_or_404(
#             queryset,
#             slug=self.kwargs["slug"],
#             organization__slug=self.kwargs["org_slug"],
#         )
#
#         # May raise a permission denied
#         self.check_object_permissions(self.request, obj)
#
#         return obj

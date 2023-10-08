from django.contrib.auth.models import User, AnonymousUser
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app_core.permissions import IsOwner
from rest_framework.response import Response

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView, get_object_or_404,
)

from app_core.models import Ticket, Location

from app_core.serializers import (
    TicketSerializer,
    LocationSerializer,
    TicketByLocationSerializer,
    TicketCreateSerializer,
    UserSerializer, TicketSerializer,
)
from app_core.tasks import task_execute


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
    lookup_field = 'pk'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])


class UserMeView(RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(User, pk=self.request.user.pk)


class TicketListView(ListAPIView):
    queryset = Ticket.objects.filter(rejected=False)
    serializer_class = TicketSerializer


class TicketDetailView(RetrieveAPIView):
    queryset = Ticket.objects.filter(rejected=False)
    serializer_class = TicketSerializer
    lookup_field = 'pk'


class TicketCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Ticket.objects.all()
    serializer_class = TicketCreateSerializer


class TicketByLocationView(ListAPIView):
    serializer_class = TicketByLocationSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        location = get_object_or_404(Location, slug=self.kwargs['slug'])
        return Ticket.objects.filter(location=location, rejected=False)


class TicketMyView(ListAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ticket.objects.filter(owner=self.request.user)


class LocationListView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Location.objects.filter(slug=self.kwargs['slug'])

# """
# OLD VIEWS
# """


# class TicketCreateView1(APIView):
#     def post(self, request):
#         ticket = TicketCreateSerializer(data=request.data)
#         code: int
#         if ticket.is_valid():
#             ticket.save()
#             code = 201
#         else:
#             code = 400
#         return Response(status=code)


# class TicketViewSet(viewsets.ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# """
# НЕ ТРОГАТЬ, ЭТО ТАСКИ CELERY
# """
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

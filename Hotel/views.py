from .models import Hotel
from .Serializer import HotelSerializer, HotelModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet


class HotelView(APIView):

    def get(self, request):
        data = Hotel.objects.all()
        hs = HotelSerializer(instance=data, many=True)
        return Response(hs.data, status=200)

    def post(self, request):
        data = request.data
        h = Hotel(name=data.get("name"), address=data.get("address"), manager_name=data.get("manager_name"),
                  manager_phone=data.get("manager_phone"), manager_email=data.get("manager_email"))
        h.save()
        return Response({"message": "data created"}, status=201)


class HotelListView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer


class HotelRetrieveView(RetrieveAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer


class HotelCreateView(CreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer


class HotelUpdateView(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer


class HotelDeleteView(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer


class HotelViewset(ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelModelSerializer

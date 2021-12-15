from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from bulkFiber.models import DataHall, Region, Cluster, Site, Az
from bulkFiber.serializers import DataHallSerializer, RegionSerializer,ClusterSerializer,AZSerializer,SiteSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class DataHallView (APIView):
    def get(self,format=None):
        """ 
        Get all the user records
        :param format: Format of the User records to return to
        :return: Returns a list of User records
        """
        dh = DataHall.objects.all()
        # print('user',user)
        serializer = DataHallSerializer(dh, many=True)
        # print('retun',serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = DataHallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DataHall_detailView(APIView):
    """Retrieve, update or delete a  instance."""
    def get_object(self, pk):
        try:
            return DataHall.objects.get(pk=pk)
        except DataHall.DoesNotExist:
            raise Http404
        
    """Retrieve a Datahall instance."""
    def get(self, request, pk, format=None):
        DataHall = self.get_object(pk)
        serializer = DataHallSerializer(DataHall)
        return Response(serializer.data)
    
    """ update a Datahall instance."""
    def put(self, request, pk, format=None):
        DataHall = self.get_object(pk)
        serializer = DataHallSerializer(DataHall, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """delete a user instance."""
    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create and retrieve all az
class SiteView (APIView):        
    def get(self,format=None):
        """ 
        Get all the user records
        :param format: Format of the User records to return to
        :return: Returns a list of User records
        """
        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# delete, retrieve and update az by id
class Site_detailView (APIView):
    
    """Retrieve, update or delete a  instance."""
    def get_object(self, pk):
        try:
            return Site.objects.get(pk=pk)
        except Site.DoesNotExist:
            raise Http404
        
    """Retrieve a Site instance."""
    def get(self, request, pk, format=None):
        site = self.get_object(pk)
        serializer = SiteSerializer(site)
        return Response(serializer.data)
    
    """ update a Site instance."""
    def put(self, request, pk, format=None):
        site = self.get_object(pk)
        serializer = SiteSerializer(site, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """delete a Site instance."""
    def delete(self, request, pk, format=None):
        site = self.get_object(pk)
        site.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# create and retrieve all az
class AzView (APIView):
    
    def get(self,format=None):
        """ 
        Get all the user records
        :param format: Format of the User records to return to
        :return: Returns a list of User records
        """
        az = Az.objects.all()
        serializer = AZSerializer(az, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AZSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# delete, retrieve and update az by id
class AZ_detailView (APIView):
    
    """Retrieve, update or delete a  instance."""
    def get_object(self, pk):
        try:
            return Az.objects.get(pk=pk)
        except Az.DoesNotExist:
            raise Http404
        
    """Retrieve an az instance."""
    def get(self, request, pk, format=None):
        az = self.get_object(pk)
        serializer = AZSerializer(az)
        return Response(serializer.data)
    
    """ update an az instance."""
    def put(self, request, pk, format=None):
        az = self.get_object(pk)
        serializer = AZSerializer(az, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """delete a user instance."""
    def delete(self, request, pk, format=None):
        az = self.get_object(pk)
        az.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create and retrieve all cluster
class ClusterView (APIView):
    
    def get(self,format=None):
        """ 
        Get all the user records
        :param format: Format of the User records to return to
        :return: Returns a list of User records
        """
        cluster = Cluster.objects.all()
        serializer = ClusterSerializer(cluster, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ClusterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# delete, retrieve and update cluster by id
class Cluster_detailView (APIView):
    
    """Retrieve, update or delete a  instance."""
    def get_object(self, pk):
        try:
            return Cluster.objects.get(pk=pk)
        except Cluster.DoesNotExist:
            raise Http404
        
    """Retrieve a cluster instance."""
    def get(self, request, pk, format=None):
        cluster = self.get_object(pk)
        serializer = ClusterSerializer(cluster)
        return Response(serializer.data)
    
    """ update a cluster instance."""
    def put(self, request, pk, format=None):
        cluster = self.get_object(pk)
        serializer = ClusterSerializer(cluster, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """delete a cluster instance."""
    def delete(self, request, pk, format=None):
        cluster = self.get_object(pk)
        cluster.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# create and retrieve all region
class RegionView (APIView):
    
    def get(self,format=None):
        """ 
        Get all the user records
        :param format: Format of the User records to return to
        :return: Returns a list of User records
        """
        region = Region.objects.all()
        serializer = RegionSerializer(region, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# create, retrieve and update region by id
class Region_detailView (APIView):
    
    """Retrieve, update or delete a  instance."""
    def get_object(self, pk):
        try:
            return Region.objects.get(pk=pk)
        except Region.DoesNotExist:
            # raise Http404
            return HttpResponse({"message":"Object Not Found"})
    """Retrieve a Region instance."""
    def get(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region)
        return JsonResponse(serializer.data, safe=False)
    
    """ update a Region instance."""
    def put(self, request, pk, format=None):
        region = self.get_object(pk)
        serializer = RegionSerializer(region, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    """delete a Region instance."""
    def delete(self, request, pk, format=None):
        region = self.get_object(pk)
        region.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
    

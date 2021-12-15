from bulkFiber.models import DataHall, Region, Cluster, Az, Site
from rest_framework import serializers



class DataHallSerializer (serializers.ModelSerializer):
    class Meta:
        model = DataHall
        fields = ['id', 'name', 'dh_site_code']

#Region serializers
class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id','country', 'region_name']

#Cluster serializers
class ClusterSerializer(serializers.ModelSerializer):
    region_names =  serializers.ReadOnlyField(source='c_region.region_name')
    class Meta:
        model = Cluster
        fields=['id','c_region','cluster_name','region_names']

#AZ serializers
class AZSerializer(serializers.ModelSerializer):
    cluster_names =  serializers.ReadOnlyField(source='az_cluster.cluster_name')
    class Meta:
        model=Az
        fields=['id','az_cluster','az_name','cluster_names']
 
 # Site serializers
class SiteSerializer(serializers.ModelSerializer):
    site_azs =  serializers.ReadOnlyField(source='site_az.az_name')
    class Meta:
        model=Site
        fields=['id','site_az','site_name','site_azs']
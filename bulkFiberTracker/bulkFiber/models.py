from django.db import models

# Create your models here.

class Region(models.Model):
    region_name = models.CharField(verbose_name='Region Name',max_length=25)
    country = models.CharField(verbose_name='Country Name',max_length=25)
    
    def __str__(self):
            return self.region_name
        
class Cluster(models.Model):
    cluster_name =models.CharField(verbose_name='cluster Name',max_length=10)
    c_region = models.ForeignKey(Region, verbose_name='Region', on_delete=models.CASCADE,null=True, related_name='clusterRegion')
    
    def __str__(self):
        return "{0}".format(self.cluster_name)

class Az(models.Model):
    az_name = models.CharField(verbose_name='AZ Name',max_length=15)
    az_cluster = models.ForeignKey(Cluster, verbose_name='Cluster', on_delete=models.CASCADE,null=True,related_name='azCluster')
    
    def __str__(self):
        return "{0}".format(self.az_name)

class Site(models.Model):
    site_name = models.CharField(verbose_name='Site Name',max_length=15)
    site_az = models.ForeignKey(Az, verbose_name='Az', on_delete=models.CASCADE,null=True,related_name='siteAz')
    
    def __str__(self):
        return "{0}".format(self.site_name)


class DataHall (models.Model):
    name=models.CharField(verbose_name='DH Name', max_length=15)
    dh_site = models.ForeignKey(Site, verbose_name='Site', on_delete=models.CASCADE,null=True, related_name='DhSite')
    


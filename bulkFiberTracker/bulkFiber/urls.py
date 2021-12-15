
from django.urls import path, include
from . import views

urlpatterns = [
    path('v1/api/test', views.index, name='index'),
    path('api/v1/getorcreateregion', views.RegionView.as_view(),name="RegionView"),
    path('api/v1/getregiondetail/<int:pk>', views.Region_detailView.as_view(),name="RegiondetailView"),
    path('api/v1/getorcreatecluster', views.ClusterView.as_view(),name="ClusterView"),
    path('api/v1/getclusterdetail/<int:pk>', views.Cluster_detailView.as_view(),name="ClusterdetailView"),
    path('api/v1/getorcreateaz', views.AzView.as_view(),name="AzView"),
    path('api/v1/getazdetail/<int:pk>', views.AZ_detailView.as_view(),name="AZdetailView"),
    path('api/v1/getorcreatesite', views.SiteView.as_view(),name="SiteView"),
    path('api/v1/getsitedetail/<int:pk>', views.Site_detailView.as_view(),name="SitedetailView"),
    path('api/v1/getdatahall', views.DataHallView.as_view(),name="DataHallView"),
    path('api/v1/dataHalldetailview/<int:pk>', views.DataHall_detailView.as_view(),name="DataHalldetailView"),

]
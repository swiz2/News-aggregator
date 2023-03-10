from . import views
from django.urls import path


urlpatterns = [
	path('',views.home ,name=" my-home"),
	path('Internationalrelations/',views.Internationalrel, name="my-Internationalrelations"),
	path('Sports/',views.Sports, name="my-Sports"),
	path('Politics/',views.Politics, name="my-Politics"),
	path('Newsmarket/',views.Newsmarket , name="my-Newsmarket"),
	path('Breakingnews/',views.Breakinnews, name="my-Breakingnews"),
	path('Weeklyhighlights/',views.Weeklyhigh, name="my-Weeklyhighlights"),
]
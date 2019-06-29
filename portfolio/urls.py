from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import jobs.views
import blog.views
#static is used to display image page.
urlpatterns = [
    path('admin/', admin.site.urls),

    #accessing template of job folder
    path('', jobs.views.home, name = 'jobs_home'),
    #path('blog/', blog.views.allblogs, name = 'bloghome'),

    #creating urls.py in blog because blog page contains multiple urls.
    path('blog/', include('blog.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


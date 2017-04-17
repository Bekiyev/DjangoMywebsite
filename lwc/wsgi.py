import sys
import os
sys.path.append('/Users/Bekif/Desktop/django1.6/src/lwc')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lwc.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

try:
	from dj_static import Cling
	application = Cling(get_wsgi_application())
except:
	pass
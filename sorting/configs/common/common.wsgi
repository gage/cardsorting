import os
import sys




sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib")))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../apps")))

# rebuild all photos
"""
from photos.models import ArticlePhoto
photos = ArticlePhoto.objects.filter(completed=False)
for photo in photos:
    photo.rebuild()
"""

os.environ["DJANGO_SETTINGS_MODULE"] = "omgtt.configs.commom.settings"

from django.core.handler.wsgi import WSGIHandler
application = WSGIHandler()

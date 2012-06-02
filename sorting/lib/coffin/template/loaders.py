from jinja2 import loaders, TemplateNotFound
from django.template.loader import BaseLoader, find_template_loader, make_origin
from django.template import TemplateDoesNotExist
from coffin.template.loader import get_template
from django.conf import settings

django_template_source_loaders = None

class Loader(BaseLoader):
    """
    A template loader to be used 
    """
    is_usable = True
    
    def load_template(self, template_name, template_dirs=None):
        try:
            if template_name.split('/', 1)[0] in settings.JINJA2_DISABLED_APPS:
                return get_django_template(template_name, template_dirs)
        except IndexError, AttributeError:
            pass
            
        try:
            template = get_template(template_name)
        except TemplateNotFound:
            raise TemplateDoesNotExist(template_name)
        return template, template.filename

def get_django_template(name, dirs=None):
    global django_template_source_loaders
    if django_template_source_loaders is None:
        loaders = []
        for loader_name in settings.JINJA2_TEMPLATE_LOADERS:
            loader = find_template_loader(loader_name)
            if loader is not None:
                loaders.append(loader)
        django_template_source_loaders = tuple(loaders)
    
    for loader in django_template_source_loaders:
        try:
            source, display_name = loader(name, dirs)
            return (source, make_origin(display_name, loader, name, dirs))
        except TemplateDoesNotExist:
            pass
    raise TemplateDoesNotExist(name)

def jinja_loader_from_django_loader(django_loader):
    """Attempts to make a conversion from the given Django loader to an
    similarly-behaving Jinja loader.

    :param django_loader: Django loader module string.
    :return: The similarly-behaving Jinja loader, or None if a similar loader
        could not be found.
    """
    for substr, func in _JINJA_LOADER_BY_DJANGO_SUBSTR.iteritems():
        if substr in django_loader:
            return func()
    return None


def _make_jinja_app_loader():
    """Makes an 'app loader' for Jinja which acts like
    :mod:`django.template.loaders.app_directories`.
    """
    from django.template.loaders.app_directories import app_template_dirs
    return loaders.FileSystemLoader(app_template_dirs)


def _make_jinja_filesystem_loader():
    """Makes a 'filesystem loader' for Jinja which acts like
    :mod:`django.template.loaders.filesystem`.
    """
    from django.conf import settings
    return loaders.FileSystemLoader(settings.TEMPLATE_DIRS)


# Determine loaders from Django's conf.
_JINJA_LOADER_BY_DJANGO_SUBSTR = { # {substr: callable, ...}
    'app_directories': _make_jinja_app_loader,
    'filesystem': _make_jinja_filesystem_loader,
}

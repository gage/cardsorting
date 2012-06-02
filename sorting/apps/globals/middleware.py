import re
from django.shortcuts import render_to_response
from django.template import RequestContext

class MobileDetectMiddleware(object):
    """
    Attempt to detect mobile browsers. 

    A better implementation would probably be based on 
    http://wurfl.sourceforge.net/
    or 
    http://www.zytrax.com/tech/web/mobile_ids.html
    """
    
    mobileRE = re.compile(r'android|fennec|iemobile|iphone|ipad|opera (?:mini|mobi)', re.IGNORECASE)
    androidRE = re.compile(r'android|fennec|iemobile|opera (?:mini|mobi)', re.IGNORECASE)
    iOS_RE = re.compile(r'ios|iphone|ipad', re.IGNORECASE)
    
    def process_request(self, request):
#        print "====== From Middleware ======"
        user_agent = request.META.get('HTTP_USER_AGENT', '')
#        print "User Agent: %s" % user_agent
        
        request.mobile_browser = bool(self.mobileRE.search(user_agent))
        request.is_android = bool(self.androidRE.search(user_agent))
        request.is_ios = bool(self.iOS_RE.search(user_agent))
        
#        print "is Mobile? %s" % request.mobile_browser
#        print "is Android? %s" % request.is_android
#        print "is iOS? %s" % request.is_ios
#        print "============================="
        return None
import os
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext

path = settings.STATIC_URL

def setCss(*args):
    css = []
    for a in args:
        _css = path+'css/'+a+'.css'
        if os.access(settings.PROJECT_PATH+'/static_files/css/'+a+'.css', os.F_OK):
            css.append(_css)
        else:
            raise Exception("No se pudo acceder al medio")
    return css

def setJs(*args):
    js = []
    for a in args:
        _js = path+'js/'+a+'.js'
        print (_js)
        if os.access(settings.PROJECT_PATH+'/static_files/js/'+a+'.js', os.F_OK):
            js.append(_js)
        else:
           raise Exception("No se pudo acceder al medio")
    return js

def error_view(request, id_err):

    error_dict = {
        'default': 'Ha ocurrido un error y la página no puede mostrarse',
        '5050': 'Acceso restringido!',
        '8080': 'Tiempo de la sesion agotado',
    }

    if id_err:
        key = srt(id_err)
        error = error_dict[key]
        ctx = {'error':error}
        return render_to_response('error.html',ctx,context_instance=RequestContext(request))
    else:
        error = error_dict['default']
        ctx = {'error':error}
        return render_to_response('error.html',ctx,context_instance=RequestContext(request))

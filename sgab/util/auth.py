from flask import session, redirect, url_for, request
from functools import wraps

@staticmethod
def is_authenticated():
    if 'usuario' in session:        
        return True

    # retorno falso        
    return False

@staticmethod
def is_active():
    if is_authenticated():
        if session['status'] == 1:                        
            return True
    
    return False

@staticmethod
def is_user_valid():
    if is_authenticated() and is_active():
        return True
    
    return False

@staticmethod
def is_admin():
    if is_authenticated():
        if session['cargo'] == 'admin':
            return True
        
        return False
    
@staticmethod
def is_user():
    if is_authenticated():
        if session['cargo'] == 'user':
            return True
        
        return False

@staticmethod   
def get_current_user():
    if is_authenticated():
        return session['usuario']

def url_atual():
    session.pop('next_url', None)
    session['next_url'] = request.url


def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):            
            if 'usuario' in session and session['cargo'] == role: 
                return f(*args, **kwargs)  
            
            return redirect(session['next_url'])
        return decorated_function
    return decorator
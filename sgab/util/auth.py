from flask import session, redirect, url_for

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
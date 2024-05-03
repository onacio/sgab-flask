from flask import session, redirect, url_for
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



def login_required(role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not is_authenticated:
                print('não autenticado')
                return redirect(url_for('admin.index'))
            
            return f(*args, **kwargs)
        return decorated_function
    return decorator

# sem passar parametro
def login_required_sem_parametro(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            print('NAO AUTENTICADO')
            return redirect(url_for('auth.logout'))
        return f(*args, **kwargs)
    return decorated_function

# Criando o decorator
def validar_acesso(func):
    def wrapper(args):
        # Aqui você pode adicionar qualquer lógica que deseja executar
        # antes de chamar a função de rota
        print("Executando o decorator antes da função de rota.")
        # Chama a função de rota original e retorna o resultado
        return func()
    # Mantenha o nome da função de rota original para evitar confusões com o Flask
    wrapper.__name__ = func.__name__
    return wrapper





# from functools import wraps
# from flask import session, request, redirect, url_for



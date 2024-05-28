TB_USUARIOS = '''
    CREATE TABLE IF NOT EXISTS tb_usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT (100) NOT NULL,
        sobrenome TEXT (200),
        usuario TEXT (100) NOT NULL UNIQUE,
        senha TEXT (100) NOT NULL,
        email TEXT (200) UNIQUE NOT NULL,
        funcao TEXT NOT NULL,
        setor TEXT (100)  NOT NULL,
        status INTEGER (1) NOT NULL
    );
'''

TB_UNIDADES = '''
    CREATE TABLE IF NOT EXISTS tb_unidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        nome TEXT (100) NOT NULL UNIQUE,
        nome_curto TEXT (100) NOT NULL UNIQUE,
        cnes INTEGER (7) NOT NULL UNIQUE,
        ine INTEGER (10) NOT NULL UNIQUE
    );
'''

TB_PEDIDOS = '''
    CREATE TABLE IF NOT EXISTS tb_pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        descricao TEXT (100) NOT NULL,
        categoria TEXT (100) NOT NULL,
        quantidade INTEGER NOT NULL,
        quantidade_liberada INTEGER NOT NULL,
        solicitante TEXT (100) NOT NULL,
        justificativa TEXT NOT NULL,
        data_finalizacao TEXT (100) NOT NULL,
        status INTEGER (1) NOT NULL        
    );
'''

TB_ITENS = '''
    CREATE TABLE IF NOT EXISTS tb_itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        descricao TEXT (100) NOT NULL,
        categoria TEXT (100) NOT NULL,               
        status INTEGER (1) NOT NULL               
    );
'''
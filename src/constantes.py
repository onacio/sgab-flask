CRAR_TABELA_PEDIDOS = '''
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        unidade TEXT NOT NULL,
        data TEXT NOT NULL
    );
'''
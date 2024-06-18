from db import Db

SQLMDLCREATE_fruta = '''
    CREATE TABLE IF NOT EXISTS fruta (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_fruta TEXT NOT NULL
    );
'''
SQLMDLCREATE_forma = '''
    CREATE TABLE IF NOT EXISTS forma (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_forma TEXT NOT NULL
    );
'''
SQLMDLCREATE_color = '''
    CREATE TABLE IF NOT EXISTS color (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_color TEXT NOT NULL
    );
'''


ver_frutas = '''SELECT * FROM fruta'''
ver_formas = '''SELECT * FROM forma'''
ver_colores = '''SELECT * FROM color'''


insertar_fruta = '''INSERT INTO fruta (nombre_fruta) VALUES '''
insertar_forma = '''INSERT INTO forma (nombre_forma) VALUES '''  
insertar_color = '''INSERT INTO color (nombre_color) VALUES '''           


SQLDDLUPDATEPART1 = '''UPDATE {tabla} SET {campo} = "'''
SQLDDLUPDATEPART2 = '''" WHERE id = '''


borrar_fruta = '''DELETE FROM fruta WHERE id = '''
borrar_forma = '''DELETE FROM forma WHERE id = '''
borrar_color = '''DELETE FROM color WHERE id = '''


buscar_fruta = '''SELECT id FROM fruta WHERE nombre_fruta LIKE '''
buscar_forma = '''SELECT id FROM forma WHERE nombre_forma LIKE '''
buscar_color = '''SELECT id FROM color WHERE nombre_color LIKE '''



class ColeccionDatos:
    DBNAME = 'datos.db'

    def __init__(self):
        self.con = Db.conectar(self.DBNAME)
        
        self.con.execute(SQLMDLCREATE_fruta)
        self.con.execute(SQLMDLCREATE_forma)
        self.con.execute(SQLMDLCREATE_color)

    def leer(self, tipo):
        if tipo == "fru":
            return self.con.execute(ver_frutas).fetchall()
        elif tipo == "for":
            return self.con.execute(ver_formas).fetchall()
        elif tipo == "col":
            return self.con.execute(ver_colores).fetchall()
        
    
    def insertar(self, nombre, tipo):
        if self.buscar(nombre, tipo) == 0:
            elstr = "('" + str(nombre) + "')"
            if tipo == "fru":
                self.con.execute(insertar_fruta + elstr)
            elif tipo == "for":
                self.con.execute(insertar_forma + elstr)
            elif tipo == "col":
                self.con.execute(insertar_color + elstr)

            self.con.commit()


    def borrar(self, nombre, tipo):
        id = self.buscar(nombre, tipo) 
        if id != 0:
            if tipo == "fru":
                self.con.execute(borrar_fruta + str(id))
            elif tipo == "for":
                self.con.execute(borrar_forma + str(id))
            elif tipo == "col":
                self.con.execute(borrar_color + str(id))

            self.con.commit()


    def buscar(self, nombre, tipo):
        resultado = 0
        elstr = '"' + str(nombre) + '"'
        if tipo == "fru":
            res = self.con.execute(buscar_fruta + elstr)
        elif tipo == "for":
            res = self.con.execute(buscar_forma + elstr)
        elif tipo == "col":
            res = self.con.execute(buscar_color + elstr)
            
        reg = res.fetchone()
        if reg != None:
            resultado = reg[0]
        return resultado 

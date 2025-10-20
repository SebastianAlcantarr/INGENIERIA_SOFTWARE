from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import contextlib



app = FastAPI()

class Nombre(BaseModel):
    titulo:str
    autor:str
    fecha_publicacion:str
    paginas:str
    disponible:bool
    etiquetas:str
    calificacion:float


@contextlib.contextmanager
def conectarse_db():
    conn = sqlite3.connect('identifier.sqlite')
    try:
        yield conn
    finally:
        conn.close()

conn = sqlite3.connect('identifier.sqlite')
@app.post("/name/id")
async def guardar_libro(data: Nombre):
    with conectarse_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                         INSERT INTO usuarios (titulo,autor,fecha_publicacion,paginas,disponible,etiquetas,calificacion)
                         VALUES (?,?,?,?,?,?,?)
                     ''', (data.titulo,data.autor,data.fecha_publicacion,data.paginas,data.disponible,data.etiquetas,data.calificacion))
            conn.commit()
            if cursor.rowcount>0:
                return {'exito':'guardado en la bd'}
            else:
                return {'error':"no se pudo guardar"}
        except sqlite3.Error as e:
            return {"error":f'Error en bd {e}'}

@app.get('/')
async def obtener_nombres():
    with conectarse_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT titulo,autor,fecha_publicacion,paginas,disponible,etiquetas,calificacion   FROM usuarios
            ''')
            var = cursor.fetchall()
            nombres = [{"Titulo": i[0], "Autor": i[1],
                        "Fecha de Publicacion":i[2],"Paginas":i[3],
                        "LIbro Disponible":i[4],"Etiquetas del libro":i[5],
                        "Calificacion":i[6]
                        }
                       for i in var]

            conn.close()
            return {"LISTADO de nombres": nombres}
        except sqlite3.Error as e:
            return {f'No se puedieron obtener los datos de la base de datos: error {e}'}


@app.get('/libro/{id}')
async def buscar_nombre(id:int):
    with conectarse_db() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''SELECT titulo from usuarios where ID=?
               ''', (id,))
            resultado = cursor.fetchone()
            conn.commit()
            conn.close()
            if resultado:
                return {f'Libro con id {id}':"Encontrado",
                        "LIbro" : f'Nombre del libro {resultado}'
                        }
            else:
                return {f'Libro con id {id}': "No encontrado"}
        except sqlite3.Error as e:
            return {f'No se puedieron obtener los datos de la base de datos: error {e}'}


@app.delete('/eliminar/{nombre}')
async def eliminar_nombre(nombre:str):
    with conectarse_db() as conn:
        try:
            var = nombre
            cursor = conn.cursor()
            cursor.execute('''DELETE from usuarios where usuario = ?
            ''', (var,))
            conn.commit()
            if cursor.rowcount > 0:
                return {"Usuario Eliminado": nombre}
            else:
                return {"Usuario no encontrado o ya eliminado": nombre}
        except sqlite3.Error as e:
            return {f'No se puedieron obtener los datos de la base de datos: error {e}'}


@app.put ('/eliminar/{id}')
async def cambiar_libro(ID:str,data:Nombre):
    with conectarse_db() as conn:
        try:
            cursor=conn.cursor()
            cursor.execute('''
            UPDATE usuarios 
            SET titulo=?,autor=?,fecha_publicacion=?,paginas=?,disponible=?,etiquetas=?,calificacion=?
            WHERE ID=?;
            ''',(data.titulo,data.autor,data.fecha_publicacion,data.paginas,data.disponible,data.etiquetas,data.calificacion,ID))
            conn.commit()

            if cursor.rowcount>0:
                return {"Exito" : f'Libro con id {ID} actualizado correctamente'}
            else:
                return {'Error': 'no se pudo actualizar el nombre'}
        except sqlite3.Error as e:
            return {'Error' : f' Error con la BD {e}'}
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import sqlite3
import contextlib
from fastapi.responses import HTMLResponse

app = FastAPI()

# --- MODELOS ---

class User(BaseModel):
    nombre: str
    apellido1: str
    apellido2: str

class LoginRequest(BaseModel):
    username: str
    password: str

# --- BASE DE DATOS (conexión existente) ---
@contextlib.contextmanager
def conectar_bd():
    conect = sqlite3.connect("identifier.sqlite")
    conect.row_factory = sqlite3.Row
    try:
        yield conect
    finally:
        conect.close()

# --- ENDPOINTS EXISTENTES (sin cambios) ---

@app.post("/guardar")
async def guardar(data: User):
    with conectar_bd() as enlace:
        try:
            cursor = enlace.cursor()
            cursor.execute('''INSERT INTO usuarios (nombre, apellido1, apellido2)
                              VALUES(?, ?, ?) ''',
                    (data.nombre, data.apellido1, data.apellido2))

            enlace.commit()

            if cursor.rowcount > 0:
                return {"Exito": "Se consiguio guardar en la base de datos"}
            else:
                return {"Error": "No se consiguo guardar en la base de datos"}

        except sqlite3.Error as error:
            return {"ERROR": f'{error}'}

@app.get("/mostrar")
async def mostrar():
    with conectar_bd() as enlace:
        try:
            cursor = enlace.cursor()
            cursor.execute('''SELECT * FROM usuarios''')

            informe = cursor.fetchall()

            return informe

        except sqlite3.Error as error:
            return {"ERROR": f'{error}'}

# --- NUEVO ENDPOINT PARA LOGIN BÁSICO (PROPUESTA) ---

@app.post("/login")
async def basic_login(request: LoginRequest):
    # Esto es un login muy básico para la propuesta
    # En un sistema real, compararías con una base de datos y usarías hashing
    if request.username == "admin" and request.password == "password":
        return {"message": "Login exitoso!", "status": "success"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
        )

# --- ENDPOINT PARA SERVIR EL HTML (sin cambios) ---

@app.get("/", response_class=HTMLResponse)
async def front():
    try:
        with open("index.html", "r") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return "no se encontro el archivo"
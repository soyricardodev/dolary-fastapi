Requerimientos:
- Python 3.8+
- SQLite

Instalación:
```
git clone https://github.com/soyricardodev/dolary.git
cd dolary
pip install -r requirements.txt
```

Ejecución:
```
uvicorn main:app
```

API:
- `GET /`: Devuelve una lista de los currencies actualizados.
- `GET /bcv`: Devuelve el valor del dolar en BCV.
- `GET /paralelo`: Devuelve el valor del dolar en Paralelo.
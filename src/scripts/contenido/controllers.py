""" Controladores del servicio 1 """



from flask import request
import psycopg2


from .queries import Query
from .clase_ejemplo import ClaseEjemplo


class ClasePokemon:
    """Clase ejemplo"""

    def __init__(self, nombre_pokemon, nombre_persona) -> None:
        pass

    datos_organizados = {"habilidaes": ["etc"]}


def endpoint_1():
    """Endpoint de ejemplo 1"""
    print("Ejecutano controlador")

    if not (
        "nombre_pokemon" in request.args.keys()
        and "nombre_persona" in request.args.keys()
    ):
        return "No se encontraron las llaves necesarias"

    nombre_pokemon = request.args.get("nombre_pokemon")
    nombre_persona = request.args.get("nombre_persona")

    datos_pokemon = ClasePokemon(nombre_pokemon, nombre_persona)

    return datos_pokemon.datos_organizados


def endpoint_2():
    """Endpoint de ejemplo 1"""

    datos_pokemon = ClaseEjemplo()
    datos_pokemon.validar(request.args)

    return datos_pokemon.datos_organizados


#------------------------------tabla_contenido_imdb---------------------
#----------------------obtener el contenido de la tabla-----------------
def obtener_contenidos():
    try:
        results = Query().buscar_contenidos()
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Consulta satisfactoria",
        "codigo": 0,
        "status": True,
        "obj": results,
    }


#------------------------------tabla_contenido_imdb---------------------
#-----------------------------------agregar contenido---------------------
def agregar_contenidos():
    try:
        # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_contenido(entrada.get("pk_id_peliculas"), entrada.get("titulo_pelicula"), entrada.get("ano_pelicula"),entrada.get("fk_id_tipo_contenido"),entrada.get("director_pelicula"),entrada.get("valor_pelicula"))
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "Se agrego satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla_contenido_imdb---------------------
#-----------------------------------agregar contenido---------------------
def editar_contenidos(pk_id_peliculas):
    try:
         # datos como un diccionario
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().editar_contenido(pk_id_peliculas, entrada.get("titulo_pelicula"), entrada.get("ano_pelicula"),entrada.get("fk_id_tipo_contenido"),entrada.get("director_pelicula"),entrada.get("valor_pelicula"))
    except psycopg2.Error as db_error:
        return {
            "msg": f"DB error: {str(db_error)}",
            "codigo": 0,
            "status": False,
            "obj": {},
        }
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}

    return {
        "msg": "contenido editado satisfactoriamente",
        "codigo": 0,
        "status": True,
        "obj": {},
    }

#------------------------------tabla_contenido_imdb---------------------
#----------------------------cued_contenido-----------------------------
def crud_contenido(pk_id_peliculas=None):
    if request.method == "GET":
        return obtener_contenidos()
    if request.method == "POST":
        return agregar_contenidos()
    if request.method == "PUT":
        return editar_contenidos(pk_id_peliculas)

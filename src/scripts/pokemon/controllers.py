""" Controladores del servicio 1 """

# pylint: disable-all

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


def obtener_pokemones():
    try:
        results = Query().buscar_pokemones()
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

def agregar_pokemones():
    try:
        entrada = request.json
    except Exception as exc:
        return {"msg": str(exc), "codigo": 0, "status": False, "obj": {}}
    
    try:
        Query().agregar_pokemon(entrada.get("id_pokemon"), entrada.get("nombre_pokemon"))
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


def crud_pokemones():
    if request.method == "GET":
        return obtener_pokemones()
    if request.method == "POST":
        return agregar_pokemones()

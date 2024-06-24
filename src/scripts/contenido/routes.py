""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_1_blueprint = Blueprint(
    "servicio_1_blueprint",
    __name__,
    url_prefix='/servicio-1',
)

servicio_1_blueprint.add_url_rule(
    "/ejemplo",
    view_func=controllers.endpoint_1,
    methods=["GET"]
)
servicio_1_blueprint.add_url_rule(
    "/ejemplo-body",
    view_func=controllers.endpoint_2,
    methods=["POST"]
)


#------------Rutas de contenido----------------------
servicio_1_blueprint.add_url_rule(
    "/contenidos",
    view_func=controllers.crud_contenido,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/contenidos/<pk_id_peliculas>",
    view_func=controllers.crud_contenido,
    methods=["PUT"]
)

#------------Rutas tipo_contenido----------------------
servicio_1_blueprint.add_url_rule(
    "/tipo_contenido",
    view_func=controllers.crud_tipo_contenido,
    methods=["GET", "POST"]
)

servicio_1_blueprint.add_url_rule(
    "/tipo_contenido/<pk_id_tipo_contenido>",
    view_func=controllers.crud_tipo_contenido,
    methods=["PUT"]
)

#------------Rutas tabla_generos----------------------
servicio_1_blueprint.add_url_rule(
    "/tabla_generos",
    view_func=controllers.crud_tabla_generos,
    methods=["GET","POST"]
)

servicio_1_blueprint.add_url_rule(
    "/tabla_generos/<pk_genero>",
    view_func=controllers.crud_tabla_generos,
    methods=["PUT"]
)

#------------Rutas union_peliculas_generos----------------------
servicio_1_blueprint.add_url_rule(
    "/union_peliculas_generos",
    view_func=controllers.crud_union_peliculas_generos,
    methods=["GET","POST"]
)





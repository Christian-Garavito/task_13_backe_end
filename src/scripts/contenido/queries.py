""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

# ------------------------tabla_contenido_imdb------------------------------------------
# 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_contenidos(self):
        """
        It does nothing.
        """

        query = """
            SELECT x.* FROM public.tabla_contenido_imdb x
        """

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                #print(response)
                #print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                #print(objeto_contenidos)

                return objeto_contenidos

# ------------------------tabla_contenido_imdb------------------------------------------
# 2. funcion agregar contenido--------------------------------------------------------------
    def agregar_contenido(self, pk_id_peliculas: int, titulo_pelicula,ano_pelicula,fk_id_tipo_contenido,director_pelicula,valor_pelicula):
        query = """
            INSERT INTO public.tabla_contenido_imdb
            (pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula)
            VALUES(%s, %s, %s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                #print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula])

# ------------------------tabla_contenido_imdb------------------------------------------
# 3. funcion para editar contenido-------------------------------------------------------------- 
    def editar_contenido(self, pk_id_peliculas: int, titulo_pelicula,ano_pelicula,fk_id_tipo_contenido,director_pelicula,valor_pelicula):
        query = """
            UPDATE public.tabla_contenido_imdb 
            SET titulo_pelicula=%s, ano_pelicula=%s, fk_id_tipo_contenido=%s, director_pelicula=%s, valor_pelicula=%s WHERE pk_id_peliculas = %s
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula,pk_id_peliculas])


# ------------------------tipo_contenido------------------------------------------
# 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_tipo_contenido(self):
        """
        It does nothing.
        """

        query = """
            SELECT x.* FROM public.tipo_contenido x
        """

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                #print(response)
                #print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                #print(objeto_contenidos)

                return objeto_contenidos

# ------------------------tabla tipo_contenido------------------------------------------
# 2. funcion agregar tipo_contenido--------------------------------------------------------------
    def agregar_tipo_contenido(self, pk_id_tipo_contenido, tipo_contenido, decripcion_contenido , valor_generado):
        query = """
            INSERT INTO public.tipo_contenido
            (pk_id_tipo_contenido, tipo_contenido, "decripcion_contenido ", valor_generado)
            VALUES(%s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                #print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(query, [pk_id_tipo_contenido, tipo_contenido, decripcion_contenido , valor_generado])

# ------------------------tabla tipo_contenido------------------------------------------
# 3. funcion para editar tipo_contenido--------------------------------------------------------------  
    def editar_tipo_contenido(self, pk_id_tipo_contenido, tipo_contenido, decripcion_contenido , valor_generado):
        query = """
            UPDATE public.tipo_contenido
            SET tipo_contenido=%s, "decripcion_contenido "=%s, valor_generado=%s WHERE pk_id_tipo_contenido=%s
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [tipo_contenido, decripcion_contenido , valor_generado,pk_id_tipo_contenido])


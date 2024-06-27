""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # ------------------------tabla_contenido_imdb------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_contenidos(self, filtros):
        """
        It does nothing.
        """
        pagina = 1
        limit = 5

        query = """SELECT 
                        tc.pk_id_peliculas
                        ,tc.titulo_pelicula
                        ,tc.ano_pelicula
                        ,tc.director_pelicula
                        ,tc.valor_pelicula
                        ,tc.fk_id_tipo_contenido 
                        ,ttc.tipo_contenido
                    FROM tabla_contenido_imdb tc
                    INNER JOIN tipo_contenido ttc
                    ON tc.fk_id_tipo_contenido = ttc.pk_id_tipo_contenido"""
        # print("--------------------------------------------------------")
        if filtros:
            condiciones = []
            for columna, valor in filtros.items():
                if columna == "pagina":
                    pagina = valor
                    # print(pagina)
                elif columna == "limit":
                    limit = valor
                else:
                    condiciones.append(f"{columna} = '{valor}'")

            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)

        pagina = int(limit) * (int(pagina) - 1)

        # ordenar la tabla
        query += f" ORDER BY pk_id_peliculas OFFSET {pagina} "
        # pagina la trae como un string y para poderlo perar hay que
        # query += f" OFFSET {(paginas-1)*int(limit)} LIMIT {limit}"
        # print(query)

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchmany(int(limit))

                columnas = [columna.name for columna in cursor.description or []]

                objeto_contenidos = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]
                return objeto_contenidos, bool(cursor.fetchone())

    # ------------------------tabla_contenido_imdb------------------------------------------
    # 2. funcion agregar contenido--------------------------------------------------------------
    def agregar_contenido(
        self,
        pk_id_peliculas: int,
        titulo_pelicula,
        ano_pelicula,
        fk_id_tipo_contenido,
        director_pelicula,
        valor_pelicula,
    ):
        query = """
            INSERT INTO public.tabla_contenido_imdb
            (pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula)
            VALUES(%s, %s, %s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                # print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(
                    query,
                    [
                        pk_id_peliculas,
                        titulo_pelicula,
                        ano_pelicula,
                        fk_id_tipo_contenido,
                        director_pelicula,
                        valor_pelicula,
                    ],
                )

    # ------------------------tabla_contenido_imdb------------------------------------------
    # 3. funcion para editar contenido--------------------------------------------------------------
    def editar_contenido(
        self,
        pk_id_peliculas: int,
        titulo_pelicula,
        ano_pelicula,
        fk_id_tipo_contenido,
        director_pelicula,
        valor_pelicula,
    ):
        query = """
            UPDATE public.tabla_contenido_imdb 
            SET titulo_pelicula=%s, ano_pelicula=%s, fk_id_tipo_contenido=%s, director_pelicula=%s, valor_pelicula=%s WHERE pk_id_peliculas = %s
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    [
                        titulo_pelicula,
                        ano_pelicula,
                        fk_id_tipo_contenido,
                        director_pelicula,
                        valor_pelicula,
                        pk_id_peliculas,
                    ],
                )

    # ------------------------tipo_contenido------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_tipo_contenido(self, filtros):
        """
        It does nothing.
        """
        pagina = 1
        limit = 20

        query = "SELECT x.* FROM public.tipo_contenido x"
        # print("--------------------------------------------------------")
        if filtros:
            condiciones = []
            for columna, valor in filtros.items():
                if columna == "pagina":
                    pagina = valor
                    # print(pagina)
                elif columna == "limit":
                    limit = valor
                else:
                    condiciones.append(f"{columna} = '{valor}'")

            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)

        pagina = int(limit) * (int(pagina) - 1)
        # ordenar la tabla
        # query += " ORDER BY pk_id_peliculas"
        query += f" ORDER BY pk_id_tipo_contenido OFFSET {pagina} LIMIT {limit}"
        # pagina la trae como un string y para poderlo perar hay que
        # query += f" OFFSET {(paginas-1)*int(limit)} LIMIT {limit}"
        # print(query)

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                # print(response)
                # print(cursor.description)

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

                # print(objeto_contenidos)

                return objeto_contenidos

    # ------------------------tabla tipo_contenido------------------------------------------
    # 2. funcion agregar tipo_contenido--------------------------------------------------------------
    def agregar_tipo_contenido(
        self, pk_id_tipo_contenido, tipo_contenido, decripcion_contenido, valor_generado
    ):
        query = """
            INSERT INTO public.tipo_contenido
            (pk_id_tipo_contenido, tipo_contenido, decripcion_contenido, valor_generado)
            VALUES(%s, %s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                # print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(
                    query,
                    [
                        pk_id_tipo_contenido,
                        tipo_contenido,
                        decripcion_contenido,
                        valor_generado,
                    ],
                )

    # ------------------------tabla tipo_contenido------------------------------------------
    # 3. funcion para editar tipo_contenido--------------------------------------------------------------
    def editar_tipo_contenido(
        self, pk_id_tipo_contenido, tipo_contenido, decripcion_contenido, valor_generado
    ):
        query = """
            UPDATE public.tipo_contenido
            SET tipo_contenido=%s, decripcion_contenido=%s, valor_generado=%s WHERE pk_id_tipo_contenido=%s
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    query,
                    [
                        tipo_contenido,
                        decripcion_contenido,
                        valor_generado,
                        pk_id_tipo_contenido,
                    ],
                )

    # ------------------------tabla_generos------------------------------------------
    # 1. funcion obtener contenido--------------------------------------------------------------
    def buscar_tabla_generos(self, filtros):
        """
        It does nothing.
        """
        pagina = 1
        limit = 20

        query = "SELECT x.* FROM public.tabla_generos x"
        # print("--------------------------------------------------------")
        if filtros:
            condiciones = []
            for columna, valor in filtros.items():
                if columna == "pagina":
                    pagina = valor
                    # print(pagina)
                elif columna == "limit":
                    limit = valor
                else:
                    condiciones.append(f"{columna} = '{valor}'")

            if condiciones:
                query += " WHERE " + " AND ".join(condiciones)

        pagina = int(limit) * (int(pagina) - 1)
        # ordenar la tabla
        # query += " ORDER BY pk_id_peliculas"
        query += f" ORDER BY pk_genero OFFSET {pagina} LIMIT {limit}"
        # pagina la trae como un string y para poderlo perar hay que
        # query += f" OFFSET {(paginas-1)*int(limit)} LIMIT {limit}"
        # print(query)

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                # print(response)
                # print(cursor.description)

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

                # print(objeto_contenidos)

                return objeto_contenidos

    # ------------------------tabla tabla_generos------------------------------------------
    # 2. funcion agregar tabla_generos--------------------------------------------------------------
    def agregar_tabla_genero(self, pk_genero, nombre_genero, descripcion_genero):
        query = """
            INSERT INTO public.tabla_generos
            (pk_genero, nombre_genero, descripcion_genero)
            VALUES(%s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                # print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(query, [pk_genero, nombre_genero, descripcion_genero])

    # ------------------------tabla tabla_generos------------------------------------------
    # 3. funcion para editar tabla_generos--------------------------------------------------------------
    def editar_tabla_genero(self, pk_genero, nombre_genero, descripcion_genero):
        query = """
            UPDATE public.tabla_generos
            SET nombre_genero=%s, descripcion_genero=%s WHERE pk_genero=%s
            """
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [nombre_genero, descripcion_genero, pk_genero])

    # ------------------------tabla union_peliculas_generos------------------------------------------
    # 1. funcion obtener union_peliculas_generos--------------------------------------------------------------
    def buscar_union_peliculas_generos(self):
        """
        It does nothing.
        """

        query = """
           SELECT x.* FROM public.union_peliculas_generos x
        """

        # contextos de python tema para estudiar
        # el cursor y la conexion solo funciona dentro del with
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                # print(response)
                # print(cursor.description)

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

                # print(objeto_contenidos)

                return objeto_contenidos

    # ------------------------tabla union_peliculas_generos------------------------------------------
    # 2. funcion agregar union_peliculas_generos--------------------------------------------------------------
    def agregar_union_peliculas_genero(self, pk_id_peliculas, pk_genero):
        query = """
            INSERT INTO public.union_peliculas_generos
            (pk_id_peliculas, pk_genero)
            VALUES(%s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                # print(cursor.mogrify(query, [pk_id_peliculas, titulo_pelicula, ano_pelicula, fk_id_tipo_contenido, director_pelicula, valor_pelicula]).decode())
                cursor.execute(query, [pk_id_peliculas, pk_genero])

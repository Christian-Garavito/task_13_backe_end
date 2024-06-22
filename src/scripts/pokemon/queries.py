""" Queries del servicio 1 """

from src.scripts.connection import Connection


class Query(Connection):
    """ > The Query class is a subclass of the Connection class """

    def buscar_pokemones(self):
        """
        It does nothing.
        """

        query = """
            SELECT x.* FROM public.tabla_pokemon x
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_pokemones = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_pokemones)

                return objeto_pokemones

    def agregar_pokemon(self, id_pokemon: int, nombre_pokemon):
        query = """
            INSERT INTO public.tabla_pokemon
            (id_pokemon, nombre_pokemon)
            VALUES(%s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_pokemon, nombre_pokemon]).decode())
                cursor.execute(query, [id_pokemon, nombre_pokemon])

from database.DB_connect import DBConnect
from model.connessione import Connessione
from model.object import Object


class DAO():
    def __init__(self):
        pass

    def getAllObjects(self):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT o.*
                           FROM objects o
                           """

        cursor.execute(query)

        for row in cursor:
            result.append(
                Object(**row)
            )

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ select e1.object_id as o1,e2.object_id as o2,count(*) as peso
                    from exhibition_objects e1, exhibition_objects e2
                    where e1.exhibition_id=e2.exhibition_id 
                    and e1.object_id<e2.object_id 
                    group by e1.object_id,e2.object_id
                    order by peso desc"""

        cursor.execute(query)

        for row in cursor:
            result.append(
                Connessione(idMap[row["o1"]],
                            idMap[row["o2"]],
                            row["peso"]
                            )
            )

        cursor.close()
        conn.close()
        return result




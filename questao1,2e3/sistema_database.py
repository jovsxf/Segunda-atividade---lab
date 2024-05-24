class SistemaDatabase:
    def __init__(self, database):
        self.db = database

    def create_Teacher(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    def get_Teacher(self):
        query = "MATCH (t:Teacher) RETURN t.name AS name"
        results = self.db.execute_query(query)
        if results:
            return {
                'name': results[0]['t']['name'],
                'ano_nasc': results[0]['t']['ano_nasc'],
                'cpf': results[0]['t']['cpf']
            }
        else:
            return None
        
    def update_Teacher(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        results = self.db.execute_query(query, parameters)
        if results:
            return {
                'name': results[0]['t']['name'],
                'cpf': results[0]['t']['cpf']
            }
        else:
            return None

    def delete_Teacher(self, name):
        query = "MATCH (t:Player {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
    
    def close(self):
            self._db.close()
            print('Conexão Encerrada')
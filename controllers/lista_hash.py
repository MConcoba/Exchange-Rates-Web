import datetime


class HashTable:
    def __init__(self, data=None):
        if data is not None:
            self.size = len(data)
            self.table = [[] for _ in range(self.size)]

            for item in data:
                self.insert(item)

    def hash(self, key):
        fecha = datetime.datetime.strptime(key['date'], '%Y-%m-%d')
        sum_ascii = sum(ord(c) for c in key['iso'])
        clave = int(fecha.timestamp()) + sum_ascii + int(key['value']) + int(key['id'])
        h = int(clave) % self.size
        #print(f'{clave} | {h}')
        return (h, clave)

    def insert(self, obj):
        print(self.size)
       # key = hash(obj['id'])
        hash_key = self.hash(obj)
        bucket = self.table[hash_key[0]]

        for i, (k, v) in enumerate(bucket):
            if k == hash_key[0]:
                # Si la llave ya está ocupada, buscamos el siguiente bucket vacío
                j = hash_key[0] + 1
                while j != hash_key[0]:
                    if j == self.size:
                        j = 0
                    if not self.table[j]:
                        self.table[j].append([hash_key[1], obj])
                        return
                    j += 1
                break
        else:
            # Si no se encontró una llave ocupada, agregamos el objeto al bucket actual
            bucket.append([hash_key[1], obj])


    def getAll(self):
        res = ""
        lista = []
        for i, bucket in enumerate(self.table):
            if len(bucket) > 0:
                n = {'index': i, **bucket[0][1]}
            else:
                n = {'index': i}
            lista.append(n)
        return lista

        #raise KeyError(key)

    def search(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key[0]]

        for i, (k, v) in enumerate(bucket):
            if v['id'] == key['id']:
                return {'index': hash_key[0], **v}

        raise KeyError(key)
    

    def remove(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key[0]]

        for i, (k) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

        raise KeyError(key)
    
    def clear(self):
        for bucket in self.table:
            bucket.clear()

    def resize(self, new_size):
        # Crear una nueva instancia de HashTable con el nuevo tamaño
        new_table = HashTable(new_size)
        # Copiar los elementos de la tabla anterior a la nueva tabla
        for bucket in self.table:
            for _, obj in bucket:
                new_table.insert(obj)
        # Actualizar el tamaño y la tabla de la instancia actual
        self.size = new_size
        self.table = new_table.table

    def sizee(self):
        return self.size
    
    def __str__(self):
        res = ""
        for i, bucket in enumerate(self.table):
            res += f"Bucket {i}: {bucket}\n"
        return res


# Creamos una instancia de la tabla hash con tamaño 100

# Creamos un objeto para almacenar
objeto = [{'id': 5, 'date': '2023-04-28', 'iso': 'GTQ', 'country': 'Guatemalan Quetzal', 'value': 7.8}, {'id': 2, 'date': '2023-04-28', 'iso': 'GTQ', 'country': 'Guatemalan Quetzal', 'value': 7.8}]
hash_table = HashTable(objeto)

# Insertamos el objeto en la tabla hash
""" for item in objeto:
    hash_table.insert(item)

print(hash_table.getAll()) """


# Para recuperar el objeto de la tabla hash, podemos usar su 'id' como clave
""" id_buscado = 1
obj_search = objeto[1]
#print(hash_table.search(obj_search))
#datos = hash_table.getAll() """
print(hash_table.getAll())
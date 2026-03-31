class HashTable:
    """
    Hash Table implementada desde cero usando:
    - buckets como lista de listas (separate chaining)
    - pares [key, value] almacenados en cada bucket

    Restricción: NO se usa dict para la lógica interna.
    """

    def __init__(self, capacity=53):
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self._capacity = int(capacity)
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0

    def _hash(self, key):
        """
        Función hash propia basada en ASCII:
        - Convierte la llave a string
        - Acumula usando un multiplicador primo
        - Reduce por el tamaño de la tabla
        """
        s = str(key)
        h = 0
        prime = 31
        for ch in s:
            h = (h * prime + ord(ch)) % self._capacity
        return h

    def set(self, key, value):
        idx = self._hash(key)
        bucket = self._buckets[idx]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return

        bucket.append([key, value])
        self._size += 1

    def get(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None

    def has(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def remove(self, key):
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                removed_value = bucket[i][1]
                bucket.pop(i)
                self._size -= 1
                return removed_value
        return None

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def debug_buckets(self):
        """
        Devuelve una representación simple para ver colisiones.
        (Solo para depuración / demos.)
        """
        out = []
        for i, bucket in enumerate(self._buckets):
            if bucket:
                out.append((i, [[k, v] for k, v in bucket]))
        return out


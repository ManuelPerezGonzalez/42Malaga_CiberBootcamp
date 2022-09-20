+------------------ LINKS DE AYUDA ------------------+

Guía inicial:

https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

+------------------ DESCRIPTIONS ------------------+

- Para esta práctica utilizaremos el lenguaje python en visual studio code. Es aconsejable usar una versión de la 3 en adelante ya que las anteriores dejaron de ser utilizadas a partir de ciertas actualizaciones de sistemas.

Blockchain es una base de datos descentralizada, formada por bloques encadenados por funciones criptográficas. Los datos (que pueden ser cualquier cosa) se almacenan en esos bloques, sin importar su orden (a excepción del primero que tiene unas características especiales y se denomina como "genesis block"), y cada vez que uno nuevo se crea la blockchain se actualiza. Cada bloque posee sus metadatos, como podría ser el timestamp, y se relacionan entre sí mediante los hash, es decir, cada uno tiene un hash propio que lleva al siguiente bloque y solo a ese, sin excepción.

- Flask es un framework de python que nos permitirá crear una interfaz web con la que podremos interactuar con la blockchain.

- Para empezar, siempre nos van a hacer falta las librerias hashlib, json y time.

El primer bloque creado y necesario para la sucesión de futuros bloques, recibe el nombre de bloque génesis y debemos crearlo a mano, dándole un valor a su proof.

(Proof) La prueba de trabajo es la forma en que los nuevos bloques son creados o minados en la blockchain, descubre un número, dificil de encontrar pero muy fácil de verificar (computacionalmente claro).

- Para entrar en nuestro entorno seguro y empezar a hacer peticiones escribimos en consola:

"source /requests/bin/activate"

y una vez dentro podemos usar el comando que queramos. Iniciamos con

"python3 blockchain.py".

- Para hacer una transacción mediante un requests primero introducimos la variable y sus características y después hacemos la petición.

t = {"sender": "pa", "recipient": "pa", "amount": 237 }

r = requests.post("http://127.0.0.1:5000/transactions/new", json=t)

Cuando reiniciamos el servicio se borran todos los requests enviados.

- Para comprobar que nuestros hashes se están construyendo correctamente, podemos hacerlo de la siguiente manera:
import hashlib

s = "last_proof" + "proof" + "last_hash"

hash = hashlib.sha256(s.encode()).hexdigest()

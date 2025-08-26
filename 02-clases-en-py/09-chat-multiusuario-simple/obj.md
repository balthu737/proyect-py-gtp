9) Chat multiusuario simple (POO + sockets + hilos)

🎯 Objetivo
Crear un servidor de chat y un cliente en consola; modelar usuarios y salas como clases; servidor concurrente (threading).

🧩 Conceptos

Diseño orientado a objetos para red: ServidorChat, ClienteChat, Sala.

Concurrencia con threading (o concurrent.futures).

Serialización de mensajes (JSON).

Limpieza de recursos, manejo de excepciones en hilos.

Funcionalidades mínimas

Conectar múltiples clientes, enviar mensajes a una sala, lista de usuarios conectados.

Ideas para ampliar

Autenticación básica, mensajes privados, comandos /me, persistencia de historial.

Migrar a asyncio como reto avanzado.
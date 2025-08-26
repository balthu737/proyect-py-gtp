7) Mini-ORM y acceso a SQLite con POO

🎯 Objetivo
Crear un mini-ORM que mapee clases a tablas SQLite: Model base con save(), delete(), get_by_id().

🧩 Conceptos

Abstracción y diseño de una API orientada a objetos para BD.

Métodos de clase vs. métodos de instancia (@classmethod).

SQL básico y sqlite3 del stdlib.

Mapeo objeto-relacional simple (atributos -> columnas).

Funcionalidades mínimas

Definir modelos (class Usuario(Model): nombre = Field(...)), crear/leer/actualizar/eliminar instancias.

Ideas para ampliar

Relaciones (one-to-many), consultas filtradas, migraciones simples.

Validaciones y manejo de transacciones.
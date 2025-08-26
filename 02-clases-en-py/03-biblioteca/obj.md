3) Biblioteca (clases, composición y persistencia simple)

🎯 Objetivo
Modelar Libro, Autor y una clase Biblioteca que contenga libros; guardar y cargar en JSON.

🧩 Conceptos

Composición (una Biblioteca contiene Libro objetos).

Serialización con json (métodos to_dict() / from_dict()).

Gestión de colecciones y búsqueda (por título, autor).

Encapsulación y separación de responsabilidades.

Funcionalidades mínimas

Añadir/eliminar libros, buscar por título, listar por autor.

Guardar biblioteca en biblioteca.json y cargarla.

Ideas para ampliar

Búsqueda avanzada (filtros), préstamos (clase Prestamo), manejo de fechas.

Tests unitarios para operaciones CRUD.
5) Sistema de gestión de tareas con clases y patrones simples (Factory)

🎯 Objetivo
Modelar Tarea como clase, Proyecto que contiene tareas y usar un Factory para crear distintos tipos de tareas (normal, crítica, programada).

🧩 Conceptos

Clases con distintos comportamientos (polimorfismo simple).

Patrón Factory para instanciar subtipo de Tarea.

Uso de enum para estados (PENDIENTE, EN_PROGRESO, COMPLETADA).

Propiedades, validaciones y métodos de cambio de estado.

Funcionalidades mínimas

CRUD de tareas dentro de proyectos, marcar como completada, listar por estado.

Ideas para ampliar

Observers: notificar (callback) a los suscriptores cuando cambia una tarea.

Exportar a CSV/JSON, tests unitarios.
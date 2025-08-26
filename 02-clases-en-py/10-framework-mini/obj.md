10) Framework mini: Plugins, metaclases y diseño avanzado

🎯 Objetivo
Diseñar un pequeño framework orientado a plugins: definir una clase base Plugin y un cargador dinámico; usar metaclases o registradores para auto-registro de plugins.

🧩 Conceptos

Metaclases o registradores (__init_subclass__) para construir registries automáticos.

Inyección de dependencias simple y diseño de API limpia.

Plugins dinámicos (carga desde archivos .py) y manejo seguro.

Patrones avanzados: Singleton, Strategy, Observer según convenga.

Funcionalidades mínimas

Definir plugins que implementen una interfaz (método run()), registrar y ejecutar plugins desde el framework.

Ideas para ampliar

Sistema de configuración, gestión de versiones de plugins, sandboxing mínimo.

Documentación automática y tests de integración para plugins.
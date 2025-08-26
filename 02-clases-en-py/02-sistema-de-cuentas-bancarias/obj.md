2) Sistema de cuentas bancarias (clases y herencia básica)

🎯 Objetivo
Modelar CuentaBancaria con operaciones depositar, retirar, y una subclase CuentaAhorros con interés.

🧩 Conceptos

Herencia simple (superclase y subclase).

Encapsulación de saldo (_saldo) y métodos públicos.

Manejo de errores mediante excepciones propias (FondosInsuficientes).

Override de métodos en la subclase.

Funcionalidades mínimas

Crear cuentas, depositar, retirar, ver saldo.

CuentaAhorros.aplicar_interes().

Ideas para ampliar

Registro de transacciones (lista dentro de la cuenta).

Transferencias entre cuentas.

Uso de classmethod/staticmethod para crear cuentas desde plantillas.
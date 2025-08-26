6) Sistema de facturación con herencia múltiple controlada y composición

🎯 Objetivo
Crear clases para Producto, LineaFactura, Factura y Cliente. Implementar descuentos y diferentes tipos de factura (B2B/B2C) con políticas distintas.

🧩 Conceptos

Composición (factura contiene líneas), separación en módulos.

Polimorfismo: diferentes políticas de cálculo del total (método calcular_total).

Uso responsable de herencia (preferir composición).

Manejo de redondeo y precision financiera (decimal.Decimal).

Funcionalidades mínimas

Crear factura, añadir líneas, calcular subtotal, impuestos y total.

Aplicar descuentos por cliente o por tipo de producto.

Ideas para ampliar

Facturación recurrente (clase que administra facturas programadas).

Serialización y export a PDF (librería externa opcional más adelante).
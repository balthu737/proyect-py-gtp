import http.server
import socketserver
import json
from urllib.parse import urlparse, parse_qs

# 1) Creamos una clase que maneje las peticiones
class MiManejador(http.server.SimpleHTTPRequestHandler):
    # Sobrescribimos el método do_GET, que se llama cada vez que llega una petición GET
    def do_GET(self):
        # urlparse separa la ruta de los parámetros (query string)
        parsed_url = urlparse(self.path)
        ruta = parsed_url.path              # ejemplo: "/saludo" o "/index.html"
        parametros = parse_qs(parsed_url.query)  # dict con parámetros GET (ej: {"nombre":["Alejo"]})

        if ruta == "/saludo":
            # Si la ruta es /saludo, devolvemos un JSON con un mensaje
            nombre = parametros.get("nombre", ["mundo"])[0]  # si hay ?nombre=..., lo usamos; si no, "mundo"

            respuesta = {
                "saludo": f"Hola, {nombre}!",
                "mensaje": "Bienvenido a mi mini servidor HTTP",
            }

            # Convertimos dict -> JSON (string)
            respuesta_json = json.dumps(respuesta, ensure_ascii=False)

            # Enviar cabeceras HTTP
            self.send_response(200)  # 200 OK
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()

            # El body debe ir en bytes, no en string
            self.wfile.write(respuesta_json.encode("utf-8"))

        else:
            # Si no es /saludo, dejamos que el SimpleHTTPRequestHandler maneje la petición
            # Esto sirve para poder mostrar archivos estáticos (ej: index.html)
            super().do_GET()


# 2) Configuración del servidor
PUERTO = 8000

with socketserver.TCPServer(("localhost", PUERTO), MiManejador) as httpd:
    print(f"Servidor corriendo en http://localhost:{PUERTO}")
    try:
        httpd.serve_forever()  # El servidor queda escuchando hasta que lo detengas con Ctrl+C
    except KeyboardInterrupt:
        print("\nServidor detenido")
        httpd.server_close()

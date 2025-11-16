import http.server
import socketserver
import webbrowser
import os

PORT = 8000

# Asegurarse de que estamos en el directorio correcto
# (Donde están index.html, style.css, etc.)
directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(directory)

# Configurar el manejador para servir archivos
Handler = http.server.SimpleHTTPRequestHandler

# Iniciar el servidor
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"¡Servidor iniciado! 🚀")
    print(f"Sirviendo en http://localhost:{PORT}")
    print("Presiona Ctrl+C para detener el servidor.")
    
    # Intentar abrir el navegador automáticamente
    try:
        webbrowser.open_new(f"http://localhost:{PORT}")
    except Exception as e:
        print(f"No se pudo abrir el navegador automáticamente: {e}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nCerrando servidor...")
        httpd.server_close()
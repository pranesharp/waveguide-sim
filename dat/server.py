# Local Server for the webpage
import http.server
import socketserver
import webbrowser
import os


page_display = "index.html" 

PORT = 6969

# Python to read current dir for localhost
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

# Automatically open the browser directly to your HTML file
webbrowser.open(f"http://localhost:{PORT}/{page_display}")

print(f"Serving files from: {os.getcwd()}")
print(f"Opening http://localhost:{PORT}/{page_display}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close()

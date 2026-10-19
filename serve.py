"""Optional local preview server. Form submissions are not stored or printed."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_POST(self):
        # Discard demonstration form data, including the sample password.
        self.rfile.read(int(self.headers.get("Content-Length", "0")))
        self.send_response(303)
        self.send_header("Location", "/submitted.html")
        self.end_headers()


if __name__ == "__main__":
    print("Open http://localhost:8765 — press Ctrl+C to stop.")
    ThreadingHTTPServer(("127.0.0.1", 8765), Handler).serve_forever()

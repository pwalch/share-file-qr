import magic
import tornado.ioloop
import tornado.web
import os.path

from qrfile.handlers import MainHandler, ImageHandler, MimedStaticFileHandler
from qrfile.network import get_local_ip_address
from qrfile.qrcodes import generate_qrcode_utf8


def share_file(file_absolute_path: str, port: int):
    tornado_app = make_app(file_absolute_path, port)
    tornado_app.listen(port)
    tornado.ioloop.IOLoop.current().start()


def make_app(file_absolute_path: str, port: int):
    local_ip_address: str = get_local_ip_address()

    file_basename: str = os.path.basename(file_absolute_path)
    file_route: str = f"file/{file_basename}"

    # Guess mime type from file content
    file_mime_type: str = magic.from_file(file_absolute_path, mime=True)

    # Generate QR code
    file_url: str = f"{local_ip_address}:{port}/{file_route}"
    qrcode_svg_utf8: bytes = generate_qrcode_utf8(file_url)

    # Print QR code URL
    qrcode_url: str = f"{local_ip_address}:{port}/qrcode.svg"
    print(f"Scan QR code there: http://{qrcode_url}")

    # Serve QR code and file
    return tornado.web.Application([
        ("/", MainHandler),
        ("/qrcode.svg", ImageHandler, {
            "qrcode_svg_utf8": qrcode_svg_utf8
        }),
        (f"/{file_route}()", MimedStaticFileHandler, {
            "path": file_absolute_path,
            "mime_type": file_mime_type
        }),
    ])  # yapf: disable

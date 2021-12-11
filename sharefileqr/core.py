import os.path
from typing import Any
from urllib.parse import quote

import tornado.ioloop
import tornado.web

from sharefileqr.handlers import ImageHandler, OctetStreamStaticFileHandler
from sharefileqr.network import get_local_ip_address
from sharefileqr.qrcodes import generate_ascii, generate_utf8_svg


def share_file(shared_file_abs_path: str, port: int, browser_display: bool) -> None:
    """Shares a file from the disk to a mobile phone.

    Arguments:
        shared_file_abs_path {str} -- absolute path to the file to be shared
        port {int} -- listening port for the HTTP server
        browser_display {bool} -- whether the user wants to see the SVG in the browser
    """

    local_ip_address: str = get_local_ip_address()

    # Define file route for HTTP server
    file_basename: str = os.path.basename(shared_file_abs_path)
    shared_file_route: str = f"file/{quote(file_basename)}"
    shared_file_url: str = f"{local_ip_address}:{port}/{shared_file_route}"

    # Create file route with appropriate path and mime type
    mimed_file_handler = (
        f"/{shared_file_route}()",
        OctetStreamStaticFileHandler,
        {"path": shared_file_abs_path},
    )

    # Generate Tornado app, with an SVG route if necessary
    tornado_app = generate_tornado_app(
        mimed_file_handler, shared_file_url, browser_display
    )

    # Give the QR code to the user
    deliver_qr_code(local_ip_address, port, shared_file_url, browser_display)
    tornado_app.listen(port)
    tornado.ioloop.IOLoop.current().start()


def deliver_qr_code(
    local_ip_address: str, port: int, shared_file_url: str, browser_display: bool
) -> None:
    """Gives the QR code to the user, depending on whether he wants it
    in the terminal or in the browser. If the user wants the QR code directly
    in the terminal, then it is printed directly to standard output. If the user
    wants it through a web browser, then a URL to an SVG image is printed to standard
    output for the user to click.
    """

    if browser_display:
        # Print QR code URL to be opened in the browser
        qrcode_url: str = f"{local_ip_address}:{port}/qrcode.svg"
        print("Click on this SVG image link to display the QR code to scan:")
        print(f"http://{qrcode_url}")
    else:
        # Print ASCII QR code directly in the terminal
        qrcode_ascii_string = generate_ascii(shared_file_url)
        print(qrcode_ascii_string)
        print("Scan the QR code above to get the file on your phone.")
        print("If it does not work, try the --browser-display option.")

    print()
    print("Press CTRL+C to exit once you got the file.")


def generate_tornado_app(
    mimed_file_handler: Any,
    shared_file_url: str,
    add_svg_handler: bool = False,
) -> tornado.web.Application:
    handlers = [mimed_file_handler]

    # If required, serve the QR code as an SVG
    if add_svg_handler:
        svg_handler = (
            "/qrcode.svg",
            ImageHandler,
            {"qrcode_svg_utf8": generate_utf8_svg(shared_file_url)},
        )
        handlers.append(svg_handler)

    return tornado.web.Application(handlers)

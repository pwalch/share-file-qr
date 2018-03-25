from io import BytesIO, StringIO
import qrcode as qr
from qrcode.image.svg import SvgImage


def generate_utf8_svg(file_url: str) -> bytes:
    bytes_handle = BytesIO()
    svg_image: SvgImage = qr.make(file_url, image_factory=SvgImage)
    svg_image.save(bytes_handle)
    return bytes_handle.getvalue()


def generate_ascii(file_url: str) -> str:
    qr_code = qr.QRCode()
    qr_code.add_data(file_url)

    string_handle = StringIO()
    qr_code.print_ascii(string_handle)
    return string_handle.getvalue()

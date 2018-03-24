from io import BytesIO
import qrcode
from qrcode.image.svg import SvgImage


def generate_qrcode_utf8(file_url: str) -> bytes:
    qrcode_handle = BytesIO()
    qrcode_svg: SvgImage = qrcode.make(file_url, image_factory=SvgImage)
    qrcode_svg.save(qrcode_handle)
    return qrcode_handle.getvalue()

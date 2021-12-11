from typing import Optional

import tornado.web


class ImageHandler(tornado.web.RequestHandler):
    def initialize(self, qrcode_svg_utf8: bytes) -> None:
        self.qrcode_svg_utf8 = qrcode_svg_utf8

    def get(self) -> None:
        self.write(self.qrcode_svg_utf8)
        self.set_header("Content-Type", "image/svg+xml; charset=utf-8")


class OctetStreamStaticFileHandler(tornado.web.StaticFileHandler):
    def initialize(self, path: str, default_filename: Optional[str] = None) -> None:
        super().initialize(path)
        # TODO: First had python-magic as a dependency, but this
        # forced users to install the C library libmagic.
        # To keep the application easy to install, this python-magic
        # dependency was removed, and the mime type is always set
        # as a blob of bytes.
        self.mime_type = "application/octet-stream"

    def set_extra_headers(self, path: str) -> None:
        self.set_header("Content-Type", self.mime_type)

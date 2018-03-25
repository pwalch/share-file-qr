import tornado.web


class ImageHandler(tornado.web.RequestHandler):
    def initialize(self, qrcode_svg_utf8):
        self.qrcode_svg_utf8 = qrcode_svg_utf8

    def get(self):
        self.write(self.qrcode_svg_utf8)
        self.set_header("Content-Type", "image/svg+xml; charset=utf-8")


class MimedStaticFileHandler(tornado.web.StaticFileHandler):
    def initialize(self, path, mime_type):
        super().initialize(path)
        self.mime_type = mime_type

    def set_extra_headers(self, path):
        self.set_header("Content-Type", self.mime_type)

from nbserverproxy.handlers import SuperviseAndProxyHandler


class StencilaHostProxyHandler(SuperviseAndProxyHandler):

    name = 'stencila-host'

    def get_cmd(self):
        return ['python', '-m', 'stencila', 'run', '{"port": %s}' % self.port]

    def options(self, path):
        origin = self.request.headers.get('Origin', '')
        self.set_header('Access-Control-Allow-Origin', origin)
        self.set_header('Access-Control-Allow-Credentials', 'true')
        self.set_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'Content-Type')
        self.set_header('Access-Control-Max-Age', '86400')


def load_jupyter_server_extension(app):
    app.log.info('Enabling Stencila Host proxy')
    app.web_app.add_handlers(
        '.*',
        [
            (
                app.base_url + 'stencila-host/(.*)',
                StencilaHostProxyHandler,
                dict(
                    state=dict(
                        base_url=app.base_url,
                        notebook_dir=app.notebook_dir
                    )
                )
            )
        ],
    )


def _jupyter_server_extension_paths():
    return [{
        'module': 'nbstencilahostproxy',
    }]

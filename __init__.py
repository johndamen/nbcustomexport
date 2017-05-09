from __future__ import print_function
import os
from nbconvert.exporters.export import HTMLExporter, exporter_map
from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
import warnings
import json


__version_info__ = (0, 1, 1)
__version__ = '.'.join(map(str, __version_info__))

APP_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
TPL_DIR = os.path.join(APP_ROOT, 'templates')


def _jupyter_nbextension_paths():
    return [dict(
        section="notebook",
        src='static',
        dest="nbcustomexport",
        require="nbcustomexport/js/nbcustomexport")]


def _jupyter_server_extension_paths():
    return [dict(module="nbcustomexport")]


def make_exporter(tpl):
    """create an exporter class for a given template file"""
    class Exporter(HTMLExporter):
        def __init__(self, *args, **kwargs):
            kwargs.update(template_file=tpl,
                          template_path=[TPL_DIR])
            super(Exporter, self).__init__(*args, **kwargs)
    return Exporter


class CustomConvertersHandler(IPythonHandler):

    """serve template data as json"""

    templates = dict()

    def get(self):
        data = []
        for k, v in sorted(self.templates.items()):
            data.append(dict(key=k, label='Custom template {}'.format(k)))
        self.set_header('Content-type', 'application/json; charset=UTF-8')
        self.finish(json.dumps(data))


def load_jupyter_server_extension(nbapp):
    nbapp.log.info("nbcustomexport HTML export ENABLED")

    # search templates
    templates = dict()
    for f in os.listdir(TPL_DIR):
        name, ext = os.path.splitext(f)
        if ext == '.tpl':
            if name in exporter_map:
                warnings.warn('template {} already exists'.format(name), UserWarning)
                continue
            templates[name] = make_exporter(name)

    # add templates to nbconvert exporters
    exporter_map.update(templates)

    # add templates to handler
    CustomConvertersHandler.templates = templates

    # setup handler for serving template data
    web_app = nbapp.web_app
    host_pattern = '.*$'
    route_pattern = url_path_join(web_app.settings['base_url'], '/nbcustomexport/list')
    web_app.add_handlers(host_pattern, [(route_pattern, CustomConvertersHandler)])


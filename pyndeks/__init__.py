import datetime
import os

from importlib.resources import files
from natsort import natsorted, ns
from jinja2 import Environment, FileSystemLoader


class Pyndeks():
    def __init__(self, ignore, baseurl, topdir):
        self.ignored = ['index.html']
        if ignore:
            self.ignored += open(ignore, 'r').read().splitlines()
        self.topdir = topdir
        env = Environment(loader=FileSystemLoader(files('pyndeks')))
        env.filters['natsort'] = lambda x: natsorted(x, alg=ns.IGNORECASE)
        env.globals['baseurl'] = baseurl
        env.globals['now'] = datetime.datetime.utcnow
        self.template = env.get_template('template.html.jinja')

    def get_dirs_and_files(self, dir):
        all_files = [f for f in os.listdir(dir) if f not in self.ignored]
        dirs = [f for f in all_files if os.path.isdir(f"{dir}/{f}")]
        files = [f for f in all_files if os.path.isfile(f"{dir}/{f}")]
        return dirs, files

    def render_dir(self, dir):
        print(f"Indexing {self.topdir}/{dir.removeprefix('./')}/")
        dirs, files = self.get_dirs_and_files(dir)
        context = {'dir': dir, 'dirs': dirs, 'files': files}
        self.template.stream(context).dump(f"{dir}/index.html")

    def render_all(self):
        os.chdir(self.topdir)
        for dir in (x[0] for x in os.walk('.') if os.path.isdir(x[0])):
            if dir.removeprefix('./') in self.ignored:
                continue
            self.render_dir(dir)

# Pyndeks

**Pyndeks** is yet another HTML directory indexer. Written in [Python 3](https://www.python.org/). Powered by [Jinja](https://jinja.palletsprojects.com/) and [Bootstrap 5](https://getbootstrap.com/). Depends on [natsort](https://github.com/SethMMorton/natsort).

## Install from source

```sh
git clone https://github.com/rwnobrega/pyndeks.git
cd pyndeks
pip install .
```

## Usage

```sh
pyndeks [-h] [--ignore IGNORE] [--baseurl BASEURL] topdir

Index generator.

positional arguments:
  topdir             Top directory to index.

options:
  -h, --help         show this help message and exit
  --ignore IGNORE    File containing ignored files.
  --baseurl BASEURL  Base URL for links.
```

## License

Pyndeks is licensed under the [MIT license](LICENSE).

## Similar projects

- [Indexer](https://github.com/joshbrunty/Indexer)
- [Generate Index Files](https://github.com/byjokese/Generate-Index-Files)

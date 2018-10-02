import sys
import warnings
import logging

warnings.filterwarnings("ignore")

from . import cli
from . import settings
from . import app

def parse(argv):
    if argv is None:
        argv = sys.argv[1:]

    ap = cli.add_options()
    options = cli.parse_options(argv, ap)
    config = settings.config_from_options(options)
    return config

def main(argv=None):
    logging.basicConfig(level=logging.DEBUG)

    config = parse(argv)

    log_level = config.get("app",{}).get("log_level", "DEBUG")
    logging.basicConfig( level=getattr(logging, log_level) )

    app.run(config)

if __name__ == "__main__":
    main(sys.argv[1:])

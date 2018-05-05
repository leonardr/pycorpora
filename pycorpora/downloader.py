import argparse
from distutils.dir_util import mkpath, copy_tree
import glob
import io
import sys
import zipfile
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

def main():

    DEFAULT_ZIP = "https://github.com/dariusk/corpora/archive/master.zip"

    parser = argparse.ArgumentParser(description="Install corpora data.")
    parser.add_argument(
        "--corpora-zip-url",
        help='URL pointing to .zip file of corpora data (defaults to current master on GitHub)',
        default=DEFAULT_ZIP
    )
    parsed = parser.parse_args()

    url = parsed.corpora_zip_url
    print("Installing corpora data from " + url)
    mkpath("./corpora-download")
    resp = urlopen(url).read()
    remote = io.BytesIO(resp)
    zf = zipfile.ZipFile(remote, "r")
    zf.extractall("corpora-download")
    try:
        data_dir = glob.glob("./corpora-download/*/data")[0]
    except IndexError:
        raise IndexError(
            "malformed corpora archive: expecting a subdirectory '*/data'")
    copy_tree(data_dir, "pycorpora/data")

if __name__ == '__main__':
    main()

#!C:\Users\pnjen\Desktop\portfolio_game\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'python-slugify==3.0.3','console_scripts','slugify'
__requires__ = 'python-slugify==3.0.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('python-slugify==3.0.3', 'console_scripts', 'slugify')()
    )
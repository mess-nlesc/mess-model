"""
Purpose: this script creates GitHub gists for all files in a directory.
Adapted from
https://jels-boulangier.medium.com/automatically-create-github-gists-for-your-medium-articles-ba689775b032
Usage: python create_gists.py <directory>
"""

import subprocess
import sys
from pathlib import Path

# Simple script which automatically creates GitHub gists using the GitHub CLI
# Note that you must be authenticated in the GitHub CLI
directory = Path(sys.argv[1])
for file in directory.iterdir():
    subprocess.run(["gh", "gist", "create", "--public", file], check=True)

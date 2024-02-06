#!/usr/bin/env python
"""_summary_
"""

from Messy import Messy

if __name__ == "__main__":

    messy = Messy(
        username='xenon',
        hostname='localhost',
        port=10022
    )

    messy.submit_job()

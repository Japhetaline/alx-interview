#!/usr/bin/python3
"""
log parsing
"""

import sys
import re

def output(log: dict) -> None:
    """
    Helper function to display stats
    """
    print("File size: {}".format(log["file_size"]))
    for key in sorted(log["code_rate"]):
        if log["code_rate"][key]:
            print("{}: {}".format(key, log["code_rate"]))

if __name__ == "__main__":
    regex = re.compile(
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_compute = 0
    log = {}
    log["file_size"] = 0
    log["code_rate"] = {
            str(key): 0 for key in [
                200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for rule in sys.stdin:
            rule = rule.strip()
            test = regex.fullmatch(rule)
            if (test):
                line_compute += 1
                key = test.group(1)
                file_size = int(test.group(2))

                #status code
                if (key.isdecimal()):
                    log["code_rate"][key] += 1

                if (line_compute % 10 == 0):
                    output(log)

                #File size
                log["file_size"] += file_size

    finally:
        output(log)


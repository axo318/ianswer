import os
import sys
from typing import List

from ianswer.common import Result
from ianswer.utils import getDefaultModel

########
# VARS #
########

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


############
# MESSAGES #
############

def wrongArgsMsg():
    s = "\n" \
        "Usage: python main.py <root-dir-path>"
    print(s)


def pathNotFoundMsg(path):
    s = f"Could not find requested path: '{path}'"
    print(s)


def retrieveQuestionMsg():
    s = "\n" \
        f"{OKGREEN}{BOLD}Question >>{ENDC}"
    return input(s)


def stopMsg():
    s = "\n" \
        f"{OKCYAN}{BOLD}Exiting...{ENDC}"
    print(s)


###########
# DISPLAY #
##########

def displayResults(results: List[Result]):
    print()
    for i, result in enumerate(results):
        print(f"{OKBLUE}{BOLD}Rank {i+1}:{ENDC} {result}")


########
# LOOP #
########

def doLoop(root_dir):
    print(f"{OKCYAN}{BOLD}Initializing ...{ENDC}")
    model = getDefaultModel(root_dir)
    model.initialize()
    print(f"{OKCYAN}{BOLD}Ready for use!{ENDC}")

    while True:
        q = retrieveQuestionMsg()
        results = model.answers(question=q)
        displayResults(results)


########
# MAIN #
########

def main(args):
    # Check arguments
    if len(args) != 2:
        wrongArgsMsg()
        return

    # Check directory exists
    root_dir = args[1]
    if not os.path.exists(root_dir):
        pathNotFoundMsg(root_dir)
        return

    doLoop(root_dir)


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        stopMsg()

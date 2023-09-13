#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

python print_fires.py
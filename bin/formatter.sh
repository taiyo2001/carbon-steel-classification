#!/bin/bash

# NOTE: exec with sh command. If you don't, you may get an error

CURRENT_DIR=$(dirname "$(readlink -f "$0")")
APP_PATH=$(dirname "$CURRENT_DIR")

TARGET_DIR=$APP_PATH/app

echo "== start setup =="

find "$TARGET_DIR" -type f \( -name "*.py" -o -name "*.ipynb" \) -exec black {} \;

echo "Black formatting completed for Python files in $TARGET_DIR"

echo "== end setup =="

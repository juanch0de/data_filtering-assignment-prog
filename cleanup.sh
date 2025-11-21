#!/bin/bash

echo "Cleaning project for GitHub upload..."

rm -rf .venv
find . -type d -name "__pycache__" -exec rm -r {} +
find . -name "*.DS_Store" -delete
rm -rf .idea .vscode

echo "Cleanup finished."


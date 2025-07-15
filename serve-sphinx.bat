@echo off
echo Starting local Sphinx documentation server...
echo Open your browser to: http://localhost:8000
echo Press Ctrl+C to stop the server
cd docs\_build\html
python -m http.server 8000


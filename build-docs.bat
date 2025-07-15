@echo off
echo Installing/updating MkDocs dependencies...
pip install -r requirements.txt

echo.
echo Building documentation...
mkdocs build

echo.
echo Documentation built successfully!
echo Static files are in: docs/site/
echo Open docs/site/index.html in your browser to view locally.

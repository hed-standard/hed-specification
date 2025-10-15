@echo off
echo Installing/updating Sphinx dependencies...
pip install -r requirements.txt

echo.
echo Building documentation...
sphinx-build -b html docs/source docs/_build/html

echo.
echo Documentation built successfully!
echo Static files are in: docs/_build/html/
echo Open docs/_build/html/index.html in your browser to view locally.

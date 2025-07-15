@echo off
echo Building Sphinx documentation...
cd docs
sphinx-build -b html source _build/html
cd ..

echo.
echo Checking links in built documentation...
linkchecker --check-extern docs/_build/html/index.html

echo.
echo Link checking complete!
pause

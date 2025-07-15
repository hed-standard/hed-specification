@echo off
echo Building Sphinx documentation...

cd /d "%~dp0"

echo.
echo Building HTML documentation...
sphinx-build -b html docs/source docs/_build/html

echo.
echo Building PDF documentation...
sphinx-build -b latex docs/source docs/_build/latex

echo.
echo Converting LaTeX to PDF...
cd docs\_build\latex
pdflatex HEDSpecification.tex
pdflatex HEDSpecification.tex
cd ..\..\..

echo.
echo Copying PDF to pdfs directory...
if not exist "docs\_build\pdfs" mkdir "docs\_build\pdfs"
copy "docs\_build\latex\HEDSpecification.pdf" "docs\_build\pdfs\"

echo.
echo Documentation built successfully!
echo HTML files are in: docs/_build/html/
echo PDF file is in: docs/_build/pdfs/HEDSpecification.pdf
echo Open docs/_build/html/index.html in your browser to view locally.

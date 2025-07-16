@echo off
echo Building Sphinx documentation...

cd /d "%~dp0"

echo.
echo Building HTML documentation...
sphinx-build -b html docs/source docs/_build/html

rem echo.
rem echo Building PDF documentation...
rem sphinx-build -b latex docs/source docs/_build/latex

rem echo.
rem echo Converting LaTeX to PDF...
rem cd docs\_build\latex
rem pdflatex HEDSpecification.tex
rem pdflatex HEDSpecification.tex
rem cd ..\..\..

rem echo.
rem echo Copying PDF to pdfs directory...
rem if not exist "docs\_build\pdfs" mkdir "docs\_build\pdfs"
rem copy "docs\_build\latex\HEDSpecification.pdf" "docs\_build\pdfs\"

rem echo.
rem echo Documentation built successfully!
rem echo HTML files are in: docs/_build/html/
rem echo PDF file is in: docs/_build/pdfs/HEDSpecification.pdf
rem echo Open docs/_build/html/index.html in your browser to view locally.

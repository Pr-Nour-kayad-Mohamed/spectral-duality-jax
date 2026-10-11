PDFLATEX = pdflatex
BIBTEX = bibtex
TARGET = main

all: compile

compile:
@echo "=========================================================="
@echo "COMPILATION DE LOUVRAGE UNIFIE EHK-SCCI-CORE"
@echo "=========================================================="
$(PDFLATEX) -interaction=nonstopmode $(TARGET).tex
-$(BIBTEX) $(TARGET)
$(PDFLATEX) -interaction=nonstopmode $(TARGET).tex
$(PDFLATEX) -interaction=nonstopmode $(TARGET).tex
@echo "=========================================================="
@echo "SUCCES : Le fichier master main.pdf a ete assemble"
@echo "=========================================================="

clean:
rm -f *.aux *.log *.toc *.out *.blg *.bbl chapitres/*.aux

# 📚 MAKEFILE AUTOMATISÉ POUR LA MONOGRAPHIE SCCI-CORE

PDFLATEX = pdflatex
BIBTEX = bibtex
TARGET = main

all: compile

compile:
@echo "=========================================================="
@echo "⚡ COMPILATION DE L'OUVRAGE UNIFIÉ EHK-SCCI-CORE"
@echo "=========================================================="
$(PDFLATEX) $(TARGET).tex
$(BIBTEX) $(TARGET)
$(PDFLATEX) $(TARGET).tex
$(PDFLATEX) $(TARGET).tex
@echo "=========================================================="
@echo "✅ SUCCÈS : Le fichier main.pdf a été généré avec succès."
@echo "=========================================================="

clean:
@echo "🧹 Purge des fichiers auxiliaires de compilation..."
rm -f *.aux *.log *.toc *.out *.blg *.bbl chapitres/*.aux

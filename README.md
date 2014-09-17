md2slides
=========

Convert markdown to presentation slides.

Its functionality resembles md2pdf but produces pdf presentation slides. I uses markdown -> pandoc + filter + xelatex -> beamer pdf here so it doesn't merge into md2pdf. A markdown -> html + js + css -> wkhtmltopdf workflow is possible but will be hard to deal with the slides semantics.

# Dependencies

1. Pandoc
2. Latex (xelatex)

# Examples

A presentation with a beamer template (beamer_template.tex). The template is optimized for Chinese presentation.

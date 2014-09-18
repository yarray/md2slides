md2slides
=========

Convert markdown to presentation slides.

Its functionality resembles md2pdf but produces pdf presentation slides. I uses a different workflow (markdown -> pandoc + filter + xelatex -> beamer pdf) here so it doesn't merge into md2pdf. The previous workflow (markdown -> html + js + css -> wkhtmltopdf) is possible but will make it hard to deal with the slides semantics.

# Dependencies

1. Pandoc
2. Latex (xelatex)

# Examples

A presentation with a beamer template (beamer_template.tex). The template is optimized for Chinese presentation. Feel free to change the template and the sample document (sample.md) and compile it using:

``` ./compile.sh sample.md beamer_template.tex ```

Then you can check the output as output.pdf.

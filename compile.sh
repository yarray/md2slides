pandoc -t beamer --filter ./parse_blocks.py --latex-engine=xelatex --template=$2 -V colortheme:seahorse -V outertheme:smoothbars $1 -o output.pdf

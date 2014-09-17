#!/usr/bin/env python

'''
To create a perfect beamer presentation, rich block items should be extended to markdown.
This scripts parses the specific multi-markdown style comments to latex directives to achieve this.

Supported Syntax:
    columns:
        %% columns %%
        %% column 0.5 %%
        ...
        %% column 0.5 %%
        ...
        %% columns end %%

    becomes beamer columns
'''

import pandocfilters as pf
import re
import logging

columns = re.compile(r'%%\s+columns\s+%%')
columns_end = re.compile(r'%%\s+columns end\s+%%')
column = re.compile(r'%%\s+column (\d+\.?\d+)\s+%%')

logging.basicConfig(filename='/tmp/log',
        level=logging.ERROR,
        )


def latex(s):
    return pf.RawBlock('latex', s)


def mk_columns(k, v, f, m):
    if k == 'Para':
        value = pf.stringify(v)
        matched = column.match(value)
        if columns.match(value):
            logging.debug(r'\begin{columns}')
            return latex(r'\begin{columns}')
        elif columns_end.match(value):
            logging.debug(r'\end{columns}')
            return latex(r'\end{columns}')
        elif matched:
            logging.debug(r'\column{%s\textwidth}' % matched.group(1))
            return latex(r'\column{%s\textwidth}' % matched.group(1))
        else:
            logging.debug(value)


if __name__ == "__main__":
    pf.toJSONFilter(mk_columns)

# -*- coding: utf-8 -*-

import sys
import os

#needs_sphinx = '1.0'

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Oracle SQL & PL/SQL Optimization for Developers'
copyright = u'2014-2025, Ian Reppel'
version = '4.0'
release = '4.0.0'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'OraclePLSQLOptimizationforDevelopersdoc'

latex_elements = { }
latex_documents = [
  ('index', 'OraclePLSQLOptimizationforDevelopers.tex', 'Oracle SQL \& PL/SQL Optimization for Developers Documentation',
   u'Ian Reppel', 'manual'),
]

man_pages = [
    ('index', 'oracleplsqloptimizationfordevelopers', 'Oracle SQL & PL/SQL Optimization for Developers Documentation',
     ['Ian Reppel'], 1)
]

texinfo_documents = [
  ('index', 'OraclePLSQLOptimizationforDevelopers', 'Oracle SQL & PL/SQL Optimization for Developers Documentation',
   u'Ian Reppel', 'OraclePLSQLOptimizationforDevelopers', 'One line description of project.',
   'Miscellaneous'),
]

epub_title = 'Oracle SQL & PL/SQL Optimization for Developers'
epub_author = u'Ian Reppel'
epub_publisher = u'Ian Reppel'
epub_copyright = u'2014-2025, Ian Reppel'
epub_exclude_files = ['search.html']

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

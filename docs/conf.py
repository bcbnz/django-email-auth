# -*- coding: utf-8 -*-

# Extensions in use
extensions = ['sphinx.ext.coverage', 'sphinxtogithub']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'django-email-auth'
copyright = u'2010, Blair Bonnett'

# Version (x.y) and release (with alpha/beta etc.)
version = '1.0'
release = '1.0a1'

# Documents not to include
unused_docs = []

# Directories not to search
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.
html_theme = 'default'

html_use_index = False

# Format for timestamp.
html_last_updated_fmt = '%b %d, %Y'

# Output file base name for HTML help builder.
htmlhelp_basename = 'django-email-authdoc'


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('newindex', 'django-email-auth.tex', u'django-email-auth Documentation',
   u'Blair Bonnett', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('newindex', 'django-email-auth', u'django-email-auth Documentation',
     [u'Blair Bonnett'], 1)
]

#!/usr/bin/env python

import os
import sys
import tempfile
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import json

# Get path
path = os.environ['PATH_TRANSLATED']

# Get query string
query = os.environ['QUERY_STRING']

# Get fileName, fileExtension, dirName and baseName
fileName, fileExtension = os.path.splitext(path)
dirName, baseName = os.path.split(fileName)

# Get config files
configs = []
head = dirName
while True:
	if head == '/':
		break
	else:
		configs.insert(0, head + '/.pandoc.ini')
		(head, tail) = os.path.split(head)

configs.insert(0, '/etc/pandoc.ini')
configs.append(dirName + '/.' + baseName + fileExtension + '.ini')

# Initialise config reader
config = configparser.ConfigParser()
config.read(configs)

options=''
if config.has_section('Pandoc'):
	# General options
	if config.has_option('Pandoc', 'data-dir') and config.get('Pandoc', 'data-dir') != '':
		options += ' --data-dir="' + config.get('Pandoc', 'data-dir') + '"'
	if config.has_option('Pandoc', 'from') and config.get('Pandoc', 'from') != '':
		options += ' --from=' + config.get('Pandoc', 'from')

	# Reader options
	if config.has_option('Pandoc', 'smart') and config.getboolean('Pandoc', 'smart'):
		options += ' --smart'
	if config.has_option('Pandoc', 'old-dashes') and config.getboolean('Pandoc', 'old-dashes'):
		options += ' --old-dashes'
	if config.has_option('Pandoc', 'base-header-level'):
		options += ' --base-header-level=' + config.getint('Pandoc', 'base-header-level')
	if config.has_option('Pandoc', 'indented-code-classes') and config.get('Pandoc', 'indented-code-classes') != '':
		options += ' --indented-code-classes="' + config.get('Pandoc', 'indented-code-classes') + '"'
	if config.has_option('Pandoc', 'normalize') and config.getboolean('Pandoc', 'normalize'):
		options += ' --normalize'
	if config.has_option('Pandoc', 'preserve-tabs') and config.getboolean('Pandoc', 'preserve-tabs'):
		options += ' --preserve-tabs'
	if config.has_option('Pandoc', 'tab-stop'):
		options += ' --tab-stop=' + config.getint('Pandoc', 'tab-stop')

	# General writer options
	if config.has_option('Pandoc', 'template') and config.get('Pandoc', 'template') != '':
		options += ' --template="' + config.get('Pandoc', 'template') + '"'
	if config.has_option('Pandoc', 'variable') and config.get('Pandoc', 'variable') != '':
		try:
			for (key, value) in json.loads(config.get('Pandoc', 'variable')).items():
				options += ' --variable="' + key + '":"' + value + '"'
		except ValueError:
			pass
	if config.has_option('Pandoc', 'no-wrap') and config.getboolean('Pandoc', 'no-wrap'):
		options += ' --no-wrap'
	if config.has_option('Pandoc', 'columns'):
		options += ' --columns=' + config.getint('Pandoc', 'columns')
	if config.has_option('Pandoc', 'table-of-contents') and config.getboolean('Pandoc', 'table-of-contents') or config.has_option('Pandoc', 'toc') and config.getboolean('Pandoc', 'toc') :
		options += ' --table-of-contents'
	if config.has_option('Pandoc', 'toc-depth'):
		options += ' --toc-depth=' + config.getint('Pandoc', 'toc-depth')
	if config.has_option('Pandoc', 'no-highlight') and config.getboolean('Pandoc', 'no-highlight'):
		options += ' --no-highlight'
	if config.has_option('Pandoc', 'highlight-style') and config.get('Pandoc', 'highlight-style') != '':
		options += ' --highlight-style=' + config.get('Pandoc', 'highlight-style')
	if config.has_option('Pandoc', 'include-in-header') and config.get('Pandoc', 'include-in-header') != '':
		try:
			for value in json.loads(config.get('Pandoc', 'include-in-header')):
				options += ' --include-in-header="' + value + '"'
		except ValueError:
			pass
	if config.has_option('Pandoc', 'include-before-body') and config.get('Pandoc', 'include-before-body') != '':
		try:
			for value in json.loads(config.get('Pandoc', 'include-before-body')):
				options += ' --include-before-body="' + value + '"'
		except ValueError:
			pass
	if config.has_option('Pandoc', 'include-after-body') and config.get('Pandoc', 'include-after-body') != '':
		try:
			for value in json.loads(config.get('Pandoc', 'include-after-body')):
				options += ' --include-after-body="' + value + '"'
		except ValueError:
			pass

	# Specific writer options
	if config.has_option('Pandoc', 'self-contained') and config.getboolean('Pandoc', 'self-contained'):
		options += ' --self-contained'
	if config.has_option('Pandoc', 'html-q-tags') and config.getboolean('Pandoc', 'html-q-tags'):
		options += ' --html-q-tags'
	if config.has_option('Pandoc', 'ascii') and config.getboolean('Pandoc', 'ascii'):
		options += ' --ascii'
	if config.has_option('Pandoc', 'chapters') and config.getboolean('Pandoc', 'chapters'):
		options += ' --chapters'
	if config.has_option('Pandoc', 'number-sections') and config.getboolean('Pandoc', 'number-sections'):
		options += ' --number-sections'
	if config.has_option('Pandoc', 'no-tex-ligatures') and config.getboolean('Pandoc', 'no-tex-ligatures'):
		options += ' --no-tex-ligatures'
	if config.has_option('Pandoc', 'listings') and config.getboolean('Pandoc', 'listings'):
		options += ' --listings'
	if config.has_option('Pandoc', 'section-divs') and config.getboolean('Pandoc', 'section-divs'):
		options += ' --section-divs'
	if config.has_option('Pandoc', 'email-obfuscation') and config.get('Pandoc', 'email-obfuscation') != '':
		options += ' --email-obfuscation=' + config.get('Pandoc', 'email-obfuscation')
	if config.has_option('Pandoc', 'id-prefix') and config.get('Pandoc', 'id-prefix') != '':
		options += ' --id-prefix="' + config.get('Pandoc', 'id-prefix') + '"'
	if config.has_option('Pandoc', 'title-prefix') and config.get('Pandoc', 'title-prefix') != '':
		options += ' --title-prefix="' + config.get('Pandoc', 'title-prefix') + '"'
	if config.has_option('Pandoc', 'css') and config.get('Pandoc', 'css') != '':
		try:
			for value in json.loads(config.get('Pandoc', 'css')):
				options += ' --css="' + value + '"'
		except ValueError:
			pass
	if config.has_option('Pandoc', 'reference-odt') and config.get('Pandoc', 'reference-odt') != '':
		options += ' --reference-odt="' + config.get('Pandoc', 'reference-odt') + '"'
	if config.has_option('Pandoc', 'latex-engine') and config.get('Pandoc', 'latex-engine') != '':
		options += ' --latex-engine=' + config.get('Pandoc', 'latex-engine')

	# Citation rendering
	if config.has_option('Pandoc', 'bibliography') and config.get('Pandoc', 'bibliography') != '':
		try:
			for value in json.loads(config.get('Pandoc', 'bibliography')):
				options += ' --bibliography="' + value + '"'
		except ValueError:
			pass
	if config.has_option('Pandoc', 'csl') and config.get('Pandoc', 'csl') != '':
		options += ' --csl="' + config.get('Pandoc', 'csl') + '"'
	if config.has_option('Pandoc', 'citation-abbreviations') and config.get('Pandoc', 'citation-abbreviations') != '':
		options += ' --citation-abbreviations="' + config.get('Pandoc', 'citation-abbreviations') + '"'
	if config.has_option('Pandoc', 'natbib') and config.getboolean('Pandoc', 'natbib'):
		options += ' --natbib'
	if config.has_option('Pandoc', 'biblatex') and config.getboolean('Pandoc', 'biblatex'):
		options += ' --biblatex'

	# Math rendering
	if config.has_option('Pandoc', 'latexmathml') and config.get('Pandoc', 'latexmathml') != '':
		options += ' --latexmathml="' + config.get('Pandoc', 'latexmathml') + '"'
	if config.has_option('Pandoc', 'mathml') and config.get('Pandoc', 'mathml') != '':
		options += ' --mathml="' + config.get('Pandoc', 'mathml') + '"'
	if config.has_option('Pandoc', 'jsmath') and config.get('Pandoc', 'jsmath') != '':
		options += ' --jsmath="' + config.get('Pandoc', 'jsmath') + '"'
	if config.has_option('Pandoc', 'mathjax') and config.get('Pandoc', 'mathjax') != '':
		options += ' --mathjax="' + config.get('Pandoc', 'mathjax') + '"'
	if config.has_option('Pandoc', 'gladtex') and config.getboolean('Pandoc', 'gladtex'):
		options += ' --gladtex'
	if config.has_option('Pandoc', 'mimetex') and config.get('Pandoc', 'mimetex') != '':
		options += ' --mimetex="' + config.get('Pandoc', 'mimetex') + '"'
	if config.has_option('Pandoc', 'webtex') and config.get('Pandoc', 'webtex') != '':
		options += ' --webtex="' + config.get('Pandoc', 'webtex') + '"'

if query == '':
	# output html5
	print "Content-type: text/html"
	print
	sys.stdout.flush()
	os.system('pandoc ' + options + ' -s -t html5 "' + path + '"')
elif query == 'html':
	# output html
	print "Content-type: text/html"
	print
	sys.stdout.flush()
	os.system('pandoc ' + options + ' -s "' + path + '"') 
elif query == 'pdf':
	# output pdf
	print 'Content-type: application/pdf'
	print 'Content-disposition: attachment; filename="' + baseName + '.pdf"'
	print
	sys.stdout.flush()
	fd, pdfFile = tempfile.mkstemp('.pdf')
	os.close(fd)
	os.system('pandoc ' + options + ' -o "' + pdfFile + '" "' + path + '"')
	f = open(pdfFile, 'r')
	print f.read()
	f.close()
	os.remove(pdfFile)
elif query == 'odt':
	# output odt
	print "Content-type: application/vnd.oasis.opendocument.text"
	print 'Content-disposition: attachment; filename="' + baseName + '.odt"'
	print
	sys.stdout.flush()
	fd, odtFile = tempfile.mkstemp('.odt')
	os.close(fd)
	os.system('pandoc ' + options + ' -o "' + odtFile + '" "' + path + '"')
	f = open(odtFile, 'r')
	print f.read()
	f.close()
	os.remove(odtFile)
elif query == 'raw':
	# output raw
	print "Content-type: text/plain"
	print
	sys.stdout.flush()
	f = open(path, 'r')
	print f.read()
	f.close()

exit(0)


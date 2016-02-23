#!/usr/bin/env python3

# Module Imports
import argparse
import subprocess
import re
import os
import sys
import logging as log

######################
# Main Class
class Main():

    def __init__(self, arguments):
        """
        Method to initialize Main() class and start the main process tests.
        """

        self.args = arguments
        self.sphinx_output = ''
        self.latex_output = ''

        self.fill_report = self.index_latex()
        
        # Initialize Logger
        log_level = 'INFO'
        if self.args.debug:
            log_level = 'DEBUG'
        log.basicConfig(
            filename = 'pdfbuildtest.log',
            filemode = 'w',
            level = log_level)

        # Manage Sphinx Output
        latex_files = os.listdir(args.output)
        sphinx_build = 'None'
        log.info("Check Sphinx Builds.")
        if self.args.sphinxoutput != None:
            log.info('Defining Sphinx Output from Command-line...')
            try:
                f = open(self.args.sphinxoutput, 'r')
                sphinx_build = f.read()
                f.close()
            except:
                sphinx_build = 'None'
        elif self.args.runsphinx or 'galera.tex' not in latex_files:
            log.info('Running Sphinx build...')
            sphinx_command = ['sphinx-build', '-b', 'latex',
                              self.args.source, self.args.output]
            sphinx_build = subprocess.check_output(sphinx_command)
            log.debug('Sphinx Build Output: %s' % sphinx_build)

        log.debug('Sphinx Build Output: %s' % sphinx_build)
        log.info("Done.")

        # Manage LaTeX Output
        latex_build = 'None'
        log.info('Check LaTeX Builds.')
        if self.args.latexoutput != None:
            log.info('Defining LaTeX Output from Command-line...')
            try:
                f = open(self.args.latexoutput, 'r')
                latex_build = f.read()
                f.close()
            except:
                latex_build = 'None'
        else:
            log.info('Running Sphinx build...')
            latex_command = ['make', '-C', args.output]
            latex_build = subprocess.check_output(latex_command)

        log.debug('LaTeX Build Output: %s' % latex_build)
        log.info('Done.')

        # Parse Output
        log.info('Parse LaTeX Output')
        regex_warning = "^(LaTeX Warning:).*"
        regex_underfull = "^(Underfull).*"
        regex_overfull = "^(Overfull).*"
        latex_fill_errors = self.parse_errors(
            latex_build, [regex_underfull, regex_overfull])

        if latex_fill_errors == []:
            log.info('No LaTeX Fill Errors Found.')
        else:
            fill_errors = self.print_fill_errors(latex_fill_errors)
        log.info('Done.')


    def parse_errors(self, text, match):
        """
        Method receives a line of text and RegEx that matches to
          common errors in LaTeX output.  Returns a list of errors
          found in the output.
        """

        log_errors = []
        split_output = text.split('\n')
        for line in split_output:
            for key in match:
                if re.match(key, line):
                    log.debug('Error Logged: %s' % line)
                    log_errors.append(line)

        return log_errors
        
    def print_fill_errors(self, errors):
        """
        Method identifies fill errors in received output, then prints its
          findings to stdout along with a rough table of contents to help
          in locating the source material in Sphinx reST.
        """
        for line in errors:
            units = line.split(' at lines ')
            if len(units) > 1:
                error_type = units[0][0:9].strip()
                linenums = units[1].split('--')
                self.update_fill_report(error_type, linenums)
        contents = self.latex_index.contents
        errors_to_report = ['Underfull', 'Overfull']
        tab_count = ['part','chapter','section','subsection', 'subsubsection','paragraph','subparagraph']
        for i in contents:
            tab = tab_count.index(i["section"])
            heading = '-' * tab + i["title"]
            print(heading)
            for error in errors_to_report:
                line = '\n' + '-' * tab + '+ '
                error_list = i["errors"][error] 
                if error_list != []:

                    for err in error_list:
                        print(line + error + '  '.join(err))


    def update_fill_report(self, error, lines):
        """
        Method updates the self.latex_index object, (object belongs to
          the TOC class, with text error text from the LaTeX intermediary
          file.
        """
        # Initialize Line Numbers
        line_start = int(lines[0]) - 1
        line_end = int(lines[1]) - 1

        # Log Text for Review
        log.info('Adding %s error.' % error)
        contents = []
        line = line_start
        while line <= line_end:
            contents.append(self.latex_contents[line])
            line += 1
        

        offending_text = contents

        index = self.latex_index.return_index(line_start)
        self.latex_index.add_error(index, error, offending_text)
        log.info('Added.')



    def index_latex(self):
        """
        Method indexes the LaTeX file, using the section headings as reference
          points.  It also initializes a dict on each section heading for recording
          errors from the LaTeX build.
        """

        # Gen List from Intermediary LaTeX File
        f = open(os.path.join(
            self.args.output, self.args.latexfile), 'r')
        self.latex_contents = f.read().split('\n')
        f.close()

        latex_sections = ['.part*', '.chapter*', '.section*',
                          '.subsection*', '.subsubsection*', 
                          '.paragraph*', '.subparagraph*']

        self.latex_index = TOCTree()
        linenumber = 1
        for line in self.latex_contents:
            for i in latex_sections:
                if re.match(i, line):
                    title = line.split('{')[1][0:-1]
                    if title != '\\textt':
                        self.latex_index.add(title, i, linenumber)
            linenumber += 1



class TOCTree():

    def __init__(self):
        """
        Method initializes the TOC class with the self.contents list object.
        """
        self.contents = []


    def add(self, node, add, index):
        """
        Method receives title, section type and line number, then initializes
          a dict object in self.contents.
        """
        text = {
            "section": add[1:-1],
            "title": node,
            "line": index,
            "errors": {
                "Underfull": [],
                "Overfull": []
            }
        }
        self.contents.append(text)

    def add_error(self, index, error_type, text):
        """
        Method adds an error message to the index object for that section
          in the LaTeX file.
        """
        self.contents[index]["errors"][error_type].append(text)

    def print_contents(self):
        """
        Method prints self.contents to stdout.  For use in development.
        """
        print(self.contents)

    def return_line(self, line):
        """
        Method returns a particular line from self.contents.
        """
        return self.contents[line]
    


    def return_index(self, line):
        """
        Method returns the index point in the TOC tree of a particular line.
           That is, for say line 11,543 it returns the section in self.contents
           that contains that line.
        """
        index = 0
        for i in self.contents:
            check = i["line"]
            if check > line:
                return index
            else:
                index += 1


# Main Process
if __name__ == '__main__':

    # Parse Arguments from the Command-line
    parser = argparse.ArgumentParser()

    # Directory Arguments
    parser.add_argument('-s', '--source',
                        default='source')
    parser.add_argument('-o', '--output',
                        default='tmp')
    parser.add_argument('-l', '--latexoutput',
                        default=None)
    parser.add_argument('-x', '--sphinxoutput',
                        default=None)
    parser.add_argument('-t', '--latexfile',
                        default='galera.tex')
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('-v', '--verbose',
                        action='store_true')
    parser.add_argument('--runsphinx', action='store_true')

    args = parser.parse_args()

    report = Main(args)
    sys.exit(0)


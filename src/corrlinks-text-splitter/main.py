import logging
import os

from gooey import Gooey, GooeyParser

log = logging.getLogger(__name__)
import argparse


class TextSplit():
    output_path = '../../output/'

    cost_per_email = 0.25
    char_count = 0
    char_max = 13000
    line_count = 0
    line_max = 100

    output_file_count = 0
    current_file = []

    text = ''
    nl = "\n"

    def in_bounds(self):
        return self.char_count < self.char_max and self.line_count < self.line_max - 1

    def write_current_file(self):
        self.output_file_count += 1
        with open(''.join([f'{self.output_path}output', str(self.output_file_count), '.txt']), "w", encoding='utf-8') as  f:
            f.write(''.join(self.current_file))
            log.info(f'len of current_file: {len(self.current_file)} count of \\n in current file: {self.current_file.count(self.nl)}  file #: {self.output_file_count}')
        self.current_file = []
        self.line_count = 0
        self.char_count = 0

    def get_args(self):
        parser = GooeyParser(description="Corrlinks textsplit")
        parser.add_argument('filename', help="name of the file to process", widget='FileChooser')
        return parser.parse_args()

    @Gooey
    def main(self):
        args = self.get_args()
        with open(args.filename, 'r', encoding='utf-8') as file:
            self.text = file.readlines()
        self.text = ''.join([line for line in self.text if line.strip() != '']) # Remove all empty lines
        log.info(f'len of input: {len(self.text)}')
        log.info(f'count of n in input: {self.text.count(self.nl)}')
        for char in self.text:
            if self.in_bounds():
                self.current_file.append(char)
                if char == '\n':
                    self.line_count += 1
                self.char_count += 1
            else:
                self.write_current_file()
        self.write_current_file()
        log.info(f'{self.output_file_count} emails to be sent')
        log.info(f'{round((self.cost_per_email * self.output_file_count),2)} cents total cost')
        log.info(f'files written to {os.path.abspath(self.output_path)}')

    def __init__(self):
        self.main()


TextSplit()
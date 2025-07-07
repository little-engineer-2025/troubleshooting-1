#!/usr/bin/env python3
import sys
import os

# Scoped private constants
class _:
    ERR_NUMBER_OF_ARGS_ZERO = 'expected some argument'
    ERR_FILENAME_NOT_FOUND = 'file \'%s\' not found'

    PATH_INDENTED = './data/indent'
    INDENT = 2

    OPEN_CURLY_BRACE = '{'
    CLOSE_CURLY_BRACE = '}'
    NEW_LINE = '\n'
    SEMICOLON = ';'
    SPACE = ' '
    SPACE_INDENT = '  '
    EMPTY = ''

    STR_TK_1 = '"'
    STR_TK_2 = '\''
    STR_TK_EMPTY = ''

def process(_if, _of):
    level = 0
    STR_TK = _.STR_TK_EMPTY
    while True:
        try:
            item = _if.read(1)
            if item == _.EMPTY:
                break
            if STR_TK == _.STR_TK_EMPTY:
                if item == _.OPEN_CURLY_BRACE:
                    level += 1
                    _of.write(item)
                    _of.write(_.NEW_LINE)
                    _of.write(_.SPACE_INDENT * level)
                elif item == _.CLOSE_CURLY_BRACE:
                    level -= 1
                    _of.write(_.NEW_LINE)
                    _of.write(_.SPACE_INDENT * level)
                    _of.write(item)
                    _of.write(_.NEW_LINE)
                    _of.write(_.SPACE_INDENT * level)
                elif item == _.NEW_LINE:
                    _of.write(item)
                    _of.write(_.SPACE_INDENT * level)
                elif item == _.SEMICOLON:
                    _of.write(item)
                    _of.write(_.NEW_LINE)
                    _of.write(_.SPACE_INDENT * level)
                elif item == _.STR_TK_1 or item == _.STR_TK_2:
                    _of.write(item)
                    STR_TK = item
                else:
                    _of.write(item)
            else:
                if item == STR_TK:
                    _of.write(item)
                    STR_TK = _.STR_TK_EMPTY
                else:
                    _of.write(item)
        except Exception as e:
            print('{}\n'.format(e))
            return

def indent(filename:str):
    assert os.path.exists(filename), _.ERR_FILENAME_NOT_FOUND.format(filename)
    output_filename = os.path.basename(filename)
    output_filename = 'indent.' + output_filename
    output_filename = _.PATH_INDENTED + '/' + output_filename
    if not os.path.exists(_.PATH_INDENTED):
        os.mkdir(_.PATH_INDENTED)
    with open(filename, 'r') as fi, open(output_filename, 'w') as fo:
        process(fi, fo)

def main():
    try:
        assert len(sys.argv) > 1, _.ERR_NUMBER_OF_ARGS_ZERO
        for filename in sys.argv[1:]:
            indent(filename)
        return 0
    except Exception as e:
        print('{}\n'.format(e))
        return 1

if __name__ == '__main__':
    sys.exit(main())


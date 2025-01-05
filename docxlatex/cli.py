import argparse
import sys

from docxlatex import Document


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'ip',
        type=str,
        help='An absolute or relative path to the input .docx file',
    )
    parser.add_argument(
        '--op',
        type=str,
        help='An absolute or relative path to the output file',
        default=None
    )
    parser.add_argument(
        '--xml',
        action='store_true',
        help='Dump the document\'s XML instead of converting to text',
    )
    parser.add_argument(
        '-l',
        action='store_true',
        default=False,
        help='Specifies that the document has been converted to "Linear" format'
    )
    args = parser.parse_args()

    try:
        doc = Document(args.ip)
        if args.xml:
            if args.op is None:
                print(doc.pprint_xml())
            else:
                with open(args.op, 'w', encoding='utf-8') as f:
                    f.write(doc.get_xml())
        else:
            if args.op is None:
                print(doc.get_text(linear_format=args.l))
            else:
                with open(args.op, 'w') as f:
                    f.write(doc.get_text(linear_format=args.l))
    except Exception as e:
        print(e)
        sys.exit(1)

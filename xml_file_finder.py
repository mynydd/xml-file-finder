import argparse
import fileinput
from pathlib import Path
from typing import Dict, List

from lxml import etree

xpath_namespaces : Dict[str,str] = {
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace" }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("xmldir", help="path of directory containing xml files")
    parser.add_argument("xpath", help="xpath expression. If '-' then an expression will be read from standard input")
    parser.add_argument("--printresult", help="print output from xpath evaluations",
            action="store_true")
    args = parser.parse_args()
    xpath_expression: str = ""
    if args.xpath == "-":
        for line in fileinput.input(files=["-"]):
            xpath_expression += line
    else:
        xpath_expression = args.xpath
    parser = etree.XMLParser(recover=True)
    for xmlfile in Path(args.xmldir).glob("**/*.xml"):
        with open(xmlfile) as f:
            tree = etree.parse(f, parser)
            result = tree.xpath(xpath_expression, namespaces=xpath_namespaces)
            if result:
                output: str = f"{xmlfile}:{result}" if args.printresult else xmlfile
                print(output)


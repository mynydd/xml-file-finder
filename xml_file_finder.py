from lxml import etree
from pathlib import Path
import sys
from typing import Dict, List

xpath_namespaces : Dict[str,str] = { 
    "tei": "http://www.tei-c.org/ns/1.0",
    "xml": "http://www.w3.org/XML/1998/namespace" }

if __name__ == "__main__":
    if len(sys.argv) > 2:
        rootdir: str = sys.argv[1]
        xpath_expression: str = sys.argv[2]
        printresult: bool = (len(sys.argv) > 3) and (sys.argv[3] == "printresult")
        parser = etree.XMLParser(recover=True)
        for xmlfile in Path(rootdir).glob("**/*.xml"):
            with open(xmlfile) as f:
                tree = etree.parse(f, parser)
                result = tree.xpath(xpath_expression, namespaces=xpath_namespaces)
                if result:
                    output: str = f"{xmlfile}:{result}" if printresult else xmlfile
                    print(output)
    else:
        print("Must supply root dir and xpath. May optionally also specify 'printresult'.")


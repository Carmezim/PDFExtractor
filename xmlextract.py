import argparse
from bs4 import BeautifulSoup
import re

content = None
output_xml = None

parser = argparse.ArgumentParser(description='files')
parser.add_argument('--input', required=True, help='input file to be parsed')
parser.add_argument('--output', required=True, help='output file to save result')
args = parser.parse_args()


if __name__ == '__main__':
    input_file = args.input
    output_file = args.output
    with open(input_file, "r", encoding="ISO-8859-1") as pdf_file:
        content = pdf_file.read()
        pdf_file.close()
        output_xml = ''.join(re.findall('<rdf:li.*?</rdf:li>', content, re.S))

    with open(output_file, 'w') as f:
        f.write(output_xml)
        f.close()
        x = BeautifulSoup(output_xml, 'lxml')
        for i in x.findAll('rdf:Seq'):
            print(i)


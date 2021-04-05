import xml.etree.ElementTree as ET
from shutil import copy2
import os

tree = ET.parse('config.xml')
root = tree.getroot()
for child in root:
    tag = child.tag
    if tag == 'file':
        file_name = child.attrib['file_name']
        source = child.attrib['source_path']
        destination = child.attrib['destination_path']
        try:
            copy2(os.path.join(source, file_name), destination)
            print(f'{file_name} has been successfully copied '
                  f'from {source} to {destination}.')
        except Exception as e:
            print(e)

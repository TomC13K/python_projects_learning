# https://www.geeksforgeeks.org/python-xml-to-json/

import json
import xmltodict
from pathlib import Path

xml_path = Path(__file__).parent / "xml/books.xml"
json_path = Path(__file__).parent / "json/books.json"

with xml_path.open() as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    json_data = json.dumps(data_dict)

    with json_path.open("w") as json_file:
        json_file.write(json_data)



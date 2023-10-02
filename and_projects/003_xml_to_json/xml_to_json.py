# https://www.geeksforgeeks.org/python-xml-to-json/

import json
import xmltodict
from pathlib import Path

path_entry = Path(__file__).parent / "xml/books.xml"
path_output = Path(__file__).parent / "json/books.json"
#
# with path_entry.open() as xml_file:
#     data_dict = xmltodict.parse(xml_file.read())
#     json_data = json.dumps(data_dict)
#
#     with path_output.open("w") as json_file:
#         json_file.write(json_data)


# generic -> to function


def change_xml_tojson(path_entry, path_output):
    with path_entry.open() as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        json_data = json.dumps(data_dict)

        with path_output.open("w") as json_file:
            json_file.write(json_data)


change_xml_tojson(path_entry, path_output)

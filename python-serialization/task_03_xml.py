#!/usr/bin/python3
"""
this module contains functt
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    function to serialize
    """

    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)

    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    function to deserialize
    """

    dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        dict[child.tag] = child.text
    return dict

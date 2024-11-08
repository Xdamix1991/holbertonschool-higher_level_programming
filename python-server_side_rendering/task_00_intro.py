#!/usr/bin/python3
"""
Module contenant une fonction pour générer des invitations avec des templates.
"""
import re


def generate_invitations(template, attendees):

    if not template:
        print("Erreur : Template is empty, no output files generated.")
        return
    elif not isinstance(template, str):
        print("Erreur : Invalid template type, expected a string.")
        return

    if not attendees:
        print("Erreur : No data provided, no output files generated.")
        return
    elif not isinstance(attendees, list) or not all(
                isinstance(attendee, dict) for attendee in attendees):
        print("Erreur : Invalid attendees type,"
              "expected a list of dictionaries.")
        return

    placeholders = re.findall(r'\{(.*?)\}', template)

    for index, attendee in enumerate(attendees):
        result_str = template
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            result_str = result_str.replace(f'{{{placeholder}}}',
                                            str(value) if value else "N/A")

        with open(f'output_{index}.txt', 'w') as file:
            file.write(result_str)

#!/usr/bin/python3
#!/usr/bin/python3

"""
Module contenant une fonction pour générer des invitations avec des templates.
"""

import re

def generate_invitations(template, attendees):

    if not template or not isinstance(template, str):
        raise TypeError("template must be a string")

    if not attendees or not isinstance(attendees, list):
        raise TypeError("attendees must be a list")


    placeholders = re.findall(r'\{(.*?)\}', template)

    for index, attendee in enumerate(attendees):
        result_str = template
        for placeholder in placeholders:
            value = attendee.get(placeholder, "N/A")
            result_str = result_str.replace(f'{{{placeholder}}}', str(value) if value else "N/A")

        with open(f'output_{index}.txt', 'w') as file:
            file.write(result_str)



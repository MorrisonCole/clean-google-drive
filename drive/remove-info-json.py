import json
import os
import tkinter as tk
from tkinter import filedialog

import jsonschema as jsonschema

schema = {
    "type": "object",
    "properties": {
        "starred": {"type": "boolean"},
        "viewers_can_download": {"type": "boolean"},
        "editors_can_edit_access": {"type": "boolean"},
        "last_modified_by_any_user": {"type": "string", "format": "date-time"},
        "last_modified_by_me": {"type": "string", "format": "date-time"},
        "content_last_modified": {"type": "string", "format": "date-time"},
        "created": {"type": "string", "format": "date-time"},
        "permissions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "role": {"type": "string"},
                    "kind": {"type": "string"},
                    "photo_link": {"type": "string", "format": "uri"},
                    "self_link": {"type": "string", "format": "uri"},
                    "email_address": {"type": "string"},
                    "domain": {"type": "string"},
                    "etag": {"type": "string"},
                    "deleted": {"type": "boolean"},
                    "pending_owner": {"type": "boolean"}
                }
            }
        },
        "title": {"type": "string"},
        "mime_type": {"type": "string"}
    },
    "required": [
        "starred", "viewers_can_download", "editors_can_edit_access",
        "content_last_modified", "created", "permissions",
        "title", "mime_type"
    ]
}


# Let the user select a target directory
def choose_directory():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askdirectory()


# find all json files (including subdirectories) in the target directory that match the schema (using jsonschema) and
# delete them. Print the file name and the error message if the file does not match the schema. Print the file name
# before deleting it. Make sure the file is not open when it is deleted.
def find_and_delete_info_files():
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".json"):
                valid = False
                with open(os.path.join(root, file), encoding="utf8") as json_file:
                    data = json.load(json_file)
                    try:
                        jsonschema.validate(data, schema)
                        valid = True
                    except jsonschema.exceptions.ValidationError as err:
                        print(err)
                # delete file if valid and print the file name that will be deleted
                if valid:
                    print("Deleting file: " + file)
                    os.remove(os.path.join(root, file))


if __name__ == '__main__':
    directory = choose_directory()
    find_and_delete_info_files()

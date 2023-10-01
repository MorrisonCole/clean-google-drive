import json
import tkinter as tk
from tkinter import filedialog


# Let the user select a target file
def choose_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfile(defaultextension='.json', filetypes=[('JSON files', '*.json')])


def print_urls():
    # Specify the file path where the JSON data is stored
    file_path = choose_file().name

    # Load JSON data from the file
    with open(file_path, 'r', encoding="utf8") as file:
        data = json.load(file)

    # Extract the 'google_maps_url' values
    google_maps_urls = [feature["properties"]["google_maps_url"] for feature in data["features"]]

    # Create a tkinter root window (it won't be displayed)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Ask the user for the output file location using a file dialog
    output_file_path = filedialog.asksaveasfilename(initialfile="extracted_google_maps_urls",
                                                    defaultextension=".txt",
                                                    filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

    # Check if the user canceled the file dialog
    if not output_file_path:
        print("Output file selection canceled.")
    else:
        # Save the 'google_maps_urls' list to the selected output file
        with open(output_file_path, 'w') as output_file:
            for url in google_maps_urls:
                output_file.write(url + '\n')

        print(f"Extracted 'google_maps_urls' list has been saved to {output_file_path}.")


if __name__ == '__main__':
    print_urls()

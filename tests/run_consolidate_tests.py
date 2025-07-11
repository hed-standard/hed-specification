import os
import json


def combine_tests(test_names, test_dir, output_path):
    combined_data = []

    # Read and concatenate the JSON data
    for test_name in test_names:
        file_name = os.path.join(test_dir, test_name)
        with open(file_name, 'r') as file:
            data = json.load(file)  # Load JSON data from the file
            combined_data.extend(data)  # Assume each JSON file contains a list and concatenate

    # Write the combined data back to a new JSON file
    with open(output_path, 'w') as output_file:
        json.dump(combined_data, output_file, indent=4)


def main(exclude_names=[], out_name='temp.json'):
    relative_dir = "json_tests"  # relative directory to read

    script_dir = os.path.dirname(os.path.abspath(__file__))  # directory of this script
    target_dir = os.path.join(script_dir, relative_dir)  # full path of the

    # Write the indicated files
    file_names = [f for f in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, f))]
    filtered_files = [f for f in file_names if not any(f.startswith(prefix) for prefix in exclude_names)]
    combine_tests(filtered_files, target_dir, os.path.join(script_dir, out_name))


if __name__ == '__main__':
    exclude_names = ['SCHEMA', 'VERSION_DEPRECATED']

    javascript_name = "javascriptTests.json"
    main(exclude_names, javascript_name)
    python_name = "python_tests.json"
    # main([], python_name)

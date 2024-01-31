import os

def read_json_config(file_path):
    try:
        with open(file_path, "r") as json_file:
            config_data = json.load(json_file)
        return config_data
    except Exception as e:
        print(f"Error reading JSON file {file_path}: {str(e)}")
        return None

def read_hl7_message_from_file(file_path):
    try:
        with open(file_path, "r") as file:
            hl7_message = file.read()
        return hl7_message
    except Exception as e:
        print(f"Error reading the file {file_path}: {str(e)}")
        return None

def write_response_to_file(response, file_path):
    try:
        with open(file_path, "w") as file:
            file.write(response)
        print(f"Response written to the file: {file_path}")
    except Exception as e:
        print(f"Error writing to the file {file_path}: {str(e)}")

def write_parsed_output_to_file(parsed_data, file_path):
    try:
        with open(file_path, "w") as file:
            file.write(str(parsed_data))
        print(f"Parsed output written to the file: {file_path}")
    except Exception as e:
        print(f"Error writing parsed output to the file {file_path}: {str(e)}")

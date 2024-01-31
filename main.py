from src.HL7Operations import parse_hl7_local
from src.IOOperations import (
    read_hl7_message_from_file,
    write_response_to_file,
    write_parsed_output_to_file,
    read_json_config
)
from src.Connection import send_hl7_message
import json
import os

if __name__ == "__main__":
    # Read parameters from the JSON config file
    config_data = read_json_config("config.json")

    if config_data:
        hl7_server_host = config_data["hl7_server"]["host"]
        hl7_server_port = config_data["hl7_server"]["port"]

        input_folder = config_data["file_paths"]["input_folder"]
        output_folder = config_data["file_paths"]["output_folder"]
        input_file = config_data["file_paths"]["input_file"]
        output_file = config_data["file_paths"]["output_file"]
        parsed_output_file = config_data["file_paths"]["parsed_output_file"]

        # Construct full paths
        input_file_path = os.path.join(input_folder, input_file)
        output_file_path = os.path.join(output_folder, output_file)
        parsed_output_file_path = os.path.join(output_folder, parsed_output_file)

        # Read the HL7 message from the input file
        hl7_message = read_hl7_message_from_file(input_file_path)

        if hl7_message:
            # Send the HL7 message to the HL7 server
            response = send_hl7_message(hl7_message, hl7_server_host, hl7_server_port)

            if response:
                # Write the response to the output file
                write_response_to_file(response, output_file_path)

                # Attempt to parse the response using the local HL7 parser
                parsed_data = parse_hl7_local(response)
                if parsed_data:
                    # Write parsed output to the specified file
                    write_parsed_output_to_file(parsed_data, parsed_output_file_path)
                    print("HL7 Message Parsed:")
                    print(parsed_data)
                else:
                    print("Failed to parse HL7 message locally.")
            else:
                print("Error: No response received from the server.")

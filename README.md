
# HL7 Test and Parsing

This Python script is designed for testing HL7 communication and parsing HL7 messages. It includes modular components for HL7 operations, I/O operations, and connection handling.

## Prerequisites

- Python 3.x installed
- Ensure `hl7` and `hl7apy` modules are installed:

  ```bash
  pip install python-hl7 hl7apy
  ```

## Project Structure

- **src/**
  - **HL7Operations.py**: Module for HL7 parsing operations.
  - **IOOperations.py**: Module for file I/O operations.
  - **Connection.py**: Module for managing HL7 server connections.
- **main.py**: Main script for executing HL7 testing and parsing.
- **config.json**: JSON configuration file for storing parameters.

## Usage

1. Configure the `config.json` file with the appropriate parameters.
2. Place your HL7 message file in the `input` folder.
3. Run the `main.py` script:

   ```bash
   python main.py
   ```
4. Check the output in the `output` folder.

## Configuration (config.json)

Adjust the parameters in the `config.json` file to match your specific HL7 server and file paths.

```json
{
    "hl7_server": {
        "host": "127.0.0.1",
        "port": 1234
    },
    "file_paths": {
        "input_folder": "input",
        "output_folder": "output",
        "input_file": "input.hl7",
        "output_file": "output.txt",
        "parsed_output_file": "HL7outputParsed.txt"
    }
}
```

## License

This project is licensed under the [MIT License](LICENSE).

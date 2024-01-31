import hl7

def parse_hl7_local(hl7_message):
    try:
        # Using the hl7 library for parsing
        parsed_message = hl7.parse(hl7_message)
        return parsed_message
    except Exception as e:
        print(f"Error parsing HL7 message locally: {str(e)}")
        return None

from textwrap import dedent

_TOOL_DEF = {
  "name": "Packaging requirements",
  "description": "List of requirements that the worker packaging shipments must follow or be aware of.",
  "input_schema": {
    "type": "object",
    "properties": {
      "requirements": {
        "type": "array",
        "description": "A list of specific requirements or rules the worker packaging shipments must adhere to.",
        "items": {
          "type": "object",
          "properties": {
            "requirement": {
              "type": "string",
              "description": "Specific requirement or rule to follow."
            },
            "source": {
              "type": "string",
              "description": "The exact source sentence or passage in the original text from which the requirement came from."
            }
          },
          "required": ["requirement"]
        }
      }
    },
    "required": ["requirements"]
  }
}

INFERENCE_SYSTEM_PROMPT = dedent(
        f"""
        You must only response in JSON format that adheres to the following schema:

        <JSON_SCHEMA>
        {_TOOL_DEF}
        </JSON_SCHEMA>
        """
    )

INFERENCE_MESSAGES_PROMPT = "Extract:\n" # Append input text before querying
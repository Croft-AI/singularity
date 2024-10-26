import re
from typing import List, Dict, Any
from models import SchemaProperty


class SchemaBuilder:
    """
    takes in properties to be extracted
    and returns OpenAI SDK tool schema
    """

    def __init__(self,
                 name: str,
                 description: str,
                 properties: List[SchemaProperty],
                 **kwargs
                 ) -> None:
        self.name = name
        self.description = description
        self.properties = properties
        self.kwargs = kwargs
        self.schema = self.__generate_properties()

    def __generate_properties(self) -> Dict[str, Any]:
        """
        takes in properties and returns openai tool schema
        """
        # ======= conduct checks =========
        self.__check_property_names()
        self.__check_schema_name()
        # ================================
        props = {}
        for prop in self.properties:
            if prop.type == "enum":
                props[prop.name] = {
                    "type": "string",
                    "description": prop.description,
                    "enum": prop.enum_options
                }
            else:
                props[prop.name] = {
                    "type": prop.type,
                    "description": prop.description
                }

        return {
            "type": "object",
            "description": self.description,
            "properties": props,
            "additionalProperties": False,
            "required": [prop.name for prop in self.properties]
        }

    def __check_property_names(self) -> None:
        """
        checks if two properties have the same name
        """
        if len(set([prop.name.lower() for prop in self.properties])) != len(self.properties):
            raise ValueError("No two properties can have the same name")

    def __check_schema_name(self) -> None:
        """
        checks if name is in appropriate format
        """
        if not re.match(r'^[a-zA-Z0-9]+$', self.name):
            raise ValueError(
                "Name can only contain alphanumeric characters")

    def get(self) -> Dict[str, Any]:
        """
        returns the tool schema
        """
        return self.schema


if __name__ == "__main__":
    builder = SchemaBuilder(
        name="GetCountryTemperatureTool",
        description="Tool for getting temperature in country",
        properties=[
            SchemaProperty(
                name="Country",
                type="string",
                description="Country to get weather for"
            ),
            SchemaProperty(
                name="unit",
                description="Unit of temperature, Fahrenheit or Celcius",
                type="enum",
                enum_options=["c", "f"]
            )
        ]
    )
    print(builder.get())

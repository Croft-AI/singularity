"""Model for extracted property"""
import re
from typing import Optional, Literal, List
from pydantic import BaseModel
from openai.types.chat.chat_completion_function_call_option_param import ChatCompletionFunctionCallOptionParam


class SchemaProperty(BaseModel):
    """
    type (string): type of property
    name (string): name of property
    description (string): description of property
    sub_property (Property): sub property, if type is array, or dictionary,
                            declare it here
    """
    type: Literal["string"] | Literal["float"] | Literal["integer"] | Literal["enum"]
    name: str
    description: str
    enum_options: Optional[List[str]] = []

    def validate_name(self):
        if not re.match(r'^[a-zA-Z0-9]+$', self.name):
            raise ValueError(
                "Name can only contain alphanumeric characters")

    def validate_sub_property(self):
        if self.type in ["enum"] and len(self.enum_options) == 0:
            raise ValueError(
                f"An enum value must be defined when type is '{self.type}'.")

    # Ensure the validation is called after initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validate_sub_property()
        self.validate_name()

from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    PromptTemplate
)
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

class Furniture(BaseModel):
  type: str = Field(descritption="The type of furniture")
  style: str = Field(description="The style of furniture")
  colour: str = Field(descritption="Colour")

furniture_request = "I'd like a blue mid century chair"

parser = PydanticOutputParser(pydantic_object=Furniture)

prompt = PromptTemplate(
  template = "Answer the user query.\n{format_instructions}\n{query}\n",
  input_variables=["query"],
  partial_variables={"format_instructions": parser.get_format_instructions()}
)

_input = prompt.format_prompt(query=furniture_request)
model = ChatOpenAI(model="gpt-4.1-nano")
output = model.predict(_input.to_string())
parsed = parser.parse(output)
print(parsed.colour)
print(parsed)
print(output)
print(parser.get_format_instructions())
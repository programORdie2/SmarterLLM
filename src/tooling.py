import json
from tool_list import tools

def generate_tool_dict():    
    """
    Generate a dictionary of tools with their names as keys and the tool dictionaries as values
    """
    
    tool_dict = {}
    for tool in tools:
        tool_dict[tool["name"]] = tool
    return tool_dict

def generate_tool_schema():
    """
    Generate a list of tool schemas in the format required by the Groq API
    
    Returns:
        list: A list of tool schemas
    """
    
    tool_schema = []
    for tool in tools:
        new_tool = {
            "type": "function",
            "function": {
                "name": tool["name"],
                "description": tool["description"],
                "parameters": tool["parameters"],
            },
        }
        tool_schema.append(new_tool)
    return tool_schema

tool_dict = generate_tool_dict()
tool_schema = generate_tool_schema()

def call_tool(name, args):
    """
    Call a tool with the given name and arguments
    
    Parameters:
        name (str): The name of the tool to call
        args (dict): The arguments to pass to the tool
    
    Returns:
        str: The result of the tool call, or an error message
    """
    
    print(f"⌛ Calling tool {name} ...", end="\r")
    
    result = tool_dict[name]["function"](**args)
    if result is not None:
        print(f"✅ Called tool {name} successfully!")
        return json.dumps(result)
    
    print("⚠️ Function call failed!")
    
    return json.dumps({"error": "Function call failed"})
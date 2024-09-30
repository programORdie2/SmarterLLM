import json
from client import client
from tooling import call_tool, tool_schema
from vars import MODEL, MAX_TOKENS, MAX_FUNCTION_CALLS

def _run_tools(messages: list):
    # Make the initial API call to Groq
    response = client.chat.completions.create(
        model=MODEL, # LLM to use
        messages=messages, # Conversation history
        stream=False,
        tools=tool_schema, # Available tools (i.e. functions) for our LLM to use
        tool_choice="auto", # Let our LLM decide when to use tools
        max_tokens=MAX_TOKENS # Maximum number of tokens to allow in our response
    )

    # Extract the response and any tool call responses
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    if tool_calls:
        # Add the LLM's response to the conversation
        messages.append(response_message)

        # Process 1 call a prompt, to pass data from one tool to another
        tool_call = tool_calls[0]
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        # Call the tool and get the response
        function_response = call_tool(function_name, function_args)

        # Add the tool response to the conversation
        messages.append(
            {
                "tool_call_id": tool_call.id, 
                "role": "tool", # Indicates this message is from tool use
                "name": function_name,
                "content": function_response,
            }
        )

        # Make a second API call with the updated conversation
        second_response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            stream=False,
            tools=tool_schema,
            tool_choice="auto",
            max_tokens=MAX_TOKENS
        )

        # Return the final response
        return second_response.choices[0].message
    
    return response_message

# imports calculate function from step 1
def run_conversation(messages: list, user_prompt: str) -> str:
    # Initialize the conversation with system and user messages
    messages.append({
        "role": "user",
        "content": user_prompt,
    })

    res = _run_tools(messages)
    messages.append({
        "role": "assistant",
        "content": res.content
    })

    tools_count = 1
    while (res.tool_calls and tools_count < MAX_FUNCTION_CALLS):
        tools_count += 1

        res = _run_tools(messages)
        messages.append({
            "role": "assistant",
            "content": res.content
        })

    return res.content
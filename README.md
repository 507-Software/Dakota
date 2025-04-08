# Axis API 2.0 "Ella"

Axis API 2.0 "Ella" is a Python package for connecting to a hosted llama instance.

## Installation

```bash
pip install axisapi2
```

## Usage

```python
import axisapi2.axisapi2 as axisapi2
import random

# Initialize the Chat class
chat = axisapi2.Chat(api_url="https://your.aiservice.com/chat/completions")

# Send a message
response = chat.send_message(input("Enter your message: "))
if response:
    print(response)  # Print the AI's response
    memory = axisapi2.Memory(memfile="chat_memory.json")
    
    # Save the response to memory
    memory.set("chat" + str(random.randrange(1, 100000)), response)
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

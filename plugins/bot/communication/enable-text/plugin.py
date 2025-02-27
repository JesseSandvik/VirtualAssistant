from src.adapter import InputPluginCore, OutputPluginCore


class TextCommunicationPlugin(InputPluginCore, OutputPluginCore):

    def get_input(self):
        return input("Enter text: ")
    
    def process_input(self, user_input: str) -> str:
        # Simple processing: convert to uppercase
        # This should use the domain logic to process the user input
        processed_input = user_input.upper()
        return processed_input
    
    def send_output(self, response):
        print(f"Response: {response}")

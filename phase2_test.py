#keep an object’s data and the functions that use that data together in one unit, usually a class/object.
# The data is the object’s state, and the functions are its behavior.
#Later rename into conversational manager
class ConversationManager:

#An instance variable is a variable that belongs to a specific object of a class.
#Each object gets its own copy, so changing it in one object does not affect the others.

    def __init__(self,client,model,system_prompt):
        self.client = client
        self.model = model
        self.system_prompt = system_prompt
        self.messages = [
            {
                "role" : "system",
                "content" : self.system_prompt
            }
        ]

    def add_user_message(self, text):
        pass

    def get_response(self):
        pass

    def chat(self, user_input):
        pass

    def clear(self):
        pass

    def get_history(self):
        pass
import os 
import json 

MEMORY_FILE ="memory.json"

def load_memory():
    if not  os.path.exists(MEMORY_FILE):
        return  []

    with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    

def save_memory(memory):
    with open(MEMORY_FILE,"w") as file:
        json.dump(memory,file, indent=4)

def remember(text):
    memory = load_memory()
    memory.append(text)
    save_memory(memory)

def get_memories():
    return load_memory()

if  __name__ == "__main__":
    remember("i eat oats in the morning")
    print(get_memories())
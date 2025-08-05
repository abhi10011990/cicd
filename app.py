# app.py

def get_message(name: str = "world") -> str:
    if not name:
        raise ValueError("Name must not be empty.")
    return f"🚀 Hello, {name}!"

if __name__ == "__main__":
    print(get_message())

def create_file(filename: str, content: str):   
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"\"{filename}\" file created successfully!")
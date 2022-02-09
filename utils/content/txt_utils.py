def get_txt(filename: str, error_message: str):
    with open(f"./utils/content/txts/{filename}.txt", mode="w") as file:
        file.write(error_message)
        return f"./utils/content/txts/{filename}.txt"

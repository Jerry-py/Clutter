def get_txt(filename: str, error_message: str):
    with open(f"{filename}.txt", mode="w") as file:
        file.write(error_message)
    with open(f"{filename}.txt", mode="rb") as file:
        return file

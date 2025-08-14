def get_formatted_name(first, last, middle=""):
    
    if middle:
        full = f"{first} {middle} {last}"
    else:
        full = f"{first} {last}"
    return full.title()

if __name__ == "__main__":
    name = get_formatted_name("ada", "lovelace")
    print(name)

    name_with_middle = get_formatted_name("john", "hooker", "lee")
    print(name_with_middle)

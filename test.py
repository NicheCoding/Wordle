def color_string(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

ans2 = color_string("G", "32")
blue_text = color_string("This is blue text.", "34")

print(ans2)

alphabet = list("abcdefghijklmnopqrstuvwxyz")  # or use string.ascii_lowercase

for i, item in enumerate(alphabet):
    if item == "y":
        alphabet[i] = "Y"  # Replace 'y' with 'Y'

print(alphabet)

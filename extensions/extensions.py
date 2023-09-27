def main():
    determine_type(input("Please type your file's name\n").strip().lower())


def determine_type(file):
    if file.endswith(".jpeg") or file.endswith(".jpg"):
        print("image/jpeg")
    elif file.endswith(".gif"):
        print("image/gif")
    elif file.endswith(".png"):
        print("image/png")
    elif file.endswith(".pdf"):
        print("application/pdf")
    elif file.endswith(".txt"):
        print("text/plain")
    elif file.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")



main()
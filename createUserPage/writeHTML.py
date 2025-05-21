def writeHTMLFile(name, hobbies):
    print("Writing HTML File...")
    print(f"Received: {name} and {hobbies}")
    with open('createUserPage/userOutputFiles/index.html', 'w') as f:
        # write beginning and html head
        f.writelines(["<!DOCTYPE html>\n", "<head>\n", "\t<title>My Hobbies and Interests</title>\n", '\t<link rel="stylesheet" href="sampleStyles.css">\n', "</head>\n"])
        # write body
        f.writelines(["<body>\n", f"\t<h1>{name}</h1>\n"])
        # write closing
        f.writelines(["</body>\n", "</html>"])
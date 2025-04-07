name =  input("File Name: ")
name = name.strip()
name =  name.lower()

if name.endswith(".gif"):
    print("image/gif")
elif name.endswith(".jpg"):
    print("image/jpeg")
elif name.endswith(".jpeg"):
    print("image/jpeg")
elif name.endswith(".png"):
    print("image/png")
elif name.endswith(".pdf"):
    print("application/pdf")
elif name.endswith(".txt"):
    print("text/plain")
elif name.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")


# match name.endswith(case):
#     case ".gif":
#         print("image/gif")
#     case ".jpg"|".jpeg":
#         print("image/jpeg")
#     case ".png":
#         print("image/png")
#     case ".pdf":
#         print("application/pdf")
#     case ".txt":
#         print("text/plain")
#     case ".zip":
#         print("application/zip")
#     case _:
#         print("application/octet-stream")

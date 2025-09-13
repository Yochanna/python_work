posts = ["My first post"]

# C = Create
posts.append("Another post")

# R = Read
print(posts)

# U = Update
posts[0] = "Edited post"

# D = Delete
posts.pop(1)

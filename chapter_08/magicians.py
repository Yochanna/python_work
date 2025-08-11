def show_magicians(names):
    for name in names:
        print(name.title())

def make_great(names):
    great = []
    for name in names:
        great.append("the Great " + name)
    return great

magicians = ["houdini", "copperfield", "angel"]

show_magicians(magicians)
great_magicians = make_great(magicians[:]) 
show_magicians(great_magicians)

print("\nOriginal list remains:")
show_magicians(magicians)

# Write to a File Program

# Open (or create) a file in write mode
file = open("myfile.txt", "w")

# Write some content into the file
file.write("Hello, this is my first file in Python!\n")
file.write("I am learning how to use file functions.\n")

# Close the file to save changes
file.close()

print("Content written successfully to myfile.txt")

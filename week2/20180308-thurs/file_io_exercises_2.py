def file_writer(file):
    with open(file, 'a') as file_handle:
        new_content = input("What would you like added to the file? ")
        file_handle.write(new_content + '\n')
    
if __name__ == "__main__":
    file_name = input("Please enter a file name: ")
    file_writer(file_name)
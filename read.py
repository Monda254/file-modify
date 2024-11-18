def read_and_modify_file():
    try:
        
        input_filename = input("Enter the name of the file to read: ")

        
        with open(input_filename, 'r') as file:
            content = file.read()

        
        modified_content = content.upper()

      
        output_filename = input("Enter the name of the file to write the modified content: ")
        with open(output_filename, 'w') as file:
            file.write(modified_content)

        
        print(f"Modified content has been successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: An error occurred while reading or writing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


read_and_modify_file()

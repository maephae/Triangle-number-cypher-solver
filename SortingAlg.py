# Define new function that takes a designated input file name via string and reads it to output an array of each item after a line break
def decode(message_file): 
    with open(message_file, 'r') as file:
        
# Run the input file and build a new array out of the lines present
        message_array = file.read().splitlines()
        
# Define upper limit of message_array
        array_size = len(message_array)
        
# Sort the original array by the inner integers in ascending order
        message_array.sort(key=lambda x: int(x.split()[0]))
        
# Build right most triangle number via encode lattice
        number_array = []
        current_number = 1
        for i in range(array_size):
            number_array.append(current_number)
            if current_number + i + 2 <= array_size:
                current_number += i + 2
            else:
                break
            
# Use triangle numbers to grab distinct strings from message_array at specified index to construct output array. num-1 used as index for W <-> N correspondence
        output_array = []
        for num in number_array:
            output_array.append(message_array[num-1])
            
# Update each string element in the output_array to get rid of numbers from encode lattice
        output_array = [''.join(x for x in line.split() if not x.isdigit()) for line in output_array]
        
# Concatenate each string in output_array plus a recurring space to make it readable
        decoded_message = ' '.join(output_array)
        # Debug check print outs

    return decoded_message

#Debug setup
message_file = decode("coding_qual_input.txt")
print(message_file)

##print(f"The state of the message_array is: {array_size}")
##print(f"The size of the message_array is: {message_array}")
##print(f"The state of the number_array is: {number_array}")
##print(f"The output_array is: {output_array}")

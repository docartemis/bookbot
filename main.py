# main.py
def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    
    word_count = len(file_contents.split())

    def count_characters(file_contents):
    #convert the string to lowercase
        file_contents = file_contents.lower()
    #initialize a dictionary to store the count of each character
        character_count = {}
    #iterate over each character in the string
        for char in file_contents:
       #check if the character is an alphabet character
            if char.isalpha():
                #if the character is not in the dictionary, add it
                if char not in character_count:
                    character_count[char] = 1
                #if the character is already in the dictionary, increment the count
                else:
                    character_count[char] += 1
        return character_count

    result = count_characters(file_contents)
    #print(result)
    #turn dictionary into a list
    result_list = list(result.items())
    #sort this list in descending order
    result_list.sort(reverse=True, key=lambda x: x[1])
    #print(result_list)
    print("---Begin report of books/frankenstein.txt---")
    
    print(f"{word_count} words were found in in the document.")
    #creat a loop to print the characters and their counts
    for char, count in result_list:
        #print(f"{char}: {count}")>>changed to the following line
        print(f"The '{char}' character was found {count} times")
#if __name__ == "__main__":
main()
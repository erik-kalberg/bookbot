import os

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_count(text):
    all_words=text.split()
    letter_frequencey = {}
    for word in all_words:
        for letter in word:
            letter = letter.lower()
            if letter not in letter_frequencey:
                letter_frequencey[letter] = 1
            else:
                letter_frequencey[letter] +=1
    return letter_frequencey

def weather_report(dictionary):
    alpha_list = []
    for item in dictionary:
        temp_dict = {}
        if item.isalpha():
            temp_dict["letter"] = item
            temp_dict["num"] = dictionary[item]
            alpha_list.append(temp_dict)
    alpha_list.sort(key=lambda x: x["num"], reverse=True)
    print(alpha_list)
    for letter in range(0,len(alpha_list)):
        print(f"The letter {alpha_list[letter]['letter']} was used {alpha_list[letter]['num']} of times.")


def main():
     # Get the directory where this script is located
    current_dir = os.path.dirname(__file__)
    
    # Construct the path to 'frankenstein.txt' relative to the script's location
    book_path = os.path.join(current_dir, "books", "frankenstein.txt")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    frequency = get_letter_count(text)
    weather_report(frequency)






main()
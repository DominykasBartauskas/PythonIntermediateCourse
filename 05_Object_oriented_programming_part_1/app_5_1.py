class Sentence:
    def __init__(self, sentence: str) -> str:
        entered_sentence = sentence
        if entered_sentence == '':
            self.sentence = "Zen of Python"
        else:
            self.sentence = sentence
        self.specific_word_lst = list(self.sentence.split(" "))


    def return_reversed(self):
        print(f'Result: {self.sentence[::-1]}')

    def convert_lowercase(self):
        print(f'Result: {self.sentence.lower()}')

    def convert_uppercase(self):
        print(f'Result: {self.sentence.upper()}')

    def return_specific_word(self):
        specific_word = int(input("Enter an index number for the word you want to print: "))
        if specific_word < len(self.specific_word_lst):
            index = specific_word - 1
            print(f"The word in position {specific_word} is '{self.specific_word_lst[index]}'")
        else:
            print("Invalid value.")

    def count_specific_symbol(self):
        specific_symbol = input("Enter the symbol that you're looking for: ")
        total_symbols = self.sentence.upper().count(specific_symbol.upper())
        print(f'Result: {total_symbols}')

    def replace_word(self):
        print(self.sentence)
        to_replace = str(input("Enter the word you want to replace: "))
        replace_with = str(input("Enter the word you want to replace with: "))
        print(self.sentence.replace(to_replace, replace_with))

    def count_all_symbols(self):
        words = len(list(self.sentence.split()))
        count_upper, count_lower, count_numbers, count_symbols, sentence_length = 0, 0, 0, 0, 0
        sentence_length = len(self.sentence)
        for element in self.sentence:
            if element.isupper() == True:
                count_upper += 1
            if element.islower() == True:
                count_lower += 1
            if element.isnumeric() == True:
                count_numbers += 1
            count_symbols = sentence_length - count_upper - count_lower - count_numbers
        print(f'The sentence contains {words} words, {count_upper} uppercase characters, {count_lower} lowercase characters, {count_symbols} symbols, {count_numbers} numbers.')

    def __str__(self):
        return self.sentence

sentence_object = Sentence(input("Please enter a sentence: "))

sentence_object.return_reversed()
sentence_object.convert_lowercase()
sentence_object.convert_uppercase()
sentence_object.return_specific_word()
sentence_object.count_specific_symbol()
sentence_object.replace_word()
sentence_object.count_all_symbols()

print(sentence_object)
"""
You are given a class called Sentence , which takes a string such as 'hello world'. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

sentence = Sentence('hello world')
sentence[1].capitalize = True
print(sentence)  # writes "hello WORLD"

"""
class Sentence:
    def __init__(self, 
                 plain_text: str):
        # todo
        self.words = plain_text.split()
        self.formatted_words = {}       # we save the formated instances.


    class CapitalizedWord:

        def __init__(self, capitalized = False) -> None:
            self.capitalized = capitalized
    
    def __getitem__(self, item) -> CapitalizedWord:
        formated = self.CapitalizedWord
        self.formatted_words[item] = formated
        return self.formatted_words[item]
    
    def __str__(self) -> str:
        result = []
        for i in range(len(self.words)):
            if i in self.formatted_words.keys():
                result.append(self.words[i].upper())
            else:
                result.append(self.words[i])

        return ' '.join(result)

# frase = Sentence("Hola amigo")
# frase[1].capitalized = True
# print(frase)
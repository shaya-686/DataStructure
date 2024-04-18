import bintrees


class WordNode:
    def __init__(self, word):
        self.word = word
        self.translates = []
        self.popularity = 0

    def __str__(self):
        return f"word: {self.word}, translates: {self.translates}, popularity: {self.popularity}"


class Dictionary:
    def __init__(self):
        self.tree = bintrees.AVLTree()

    def insert_word(self, word):
        if word not in self.tree:
            new_word = WordNode(word)
            self.tree.insert(key=word, value=new_word)
        else:
            raise ValueError("Existing word")

    def delete_word(self, word):
        if word in self.tree:
            self.tree.remove(word)
        else:
            raise ValueError("Word doesn't exist")

    def update_word(self, word, new_word):
        if word in self.tree:
            word_obj = WordNode(new_word)
            self.tree.remove(word)
            self.tree[new_word] = word_obj
        else:
            raise ValueError("Word doesn't exist")

    def add_translation(self, word, translation):
        if word in self.tree:
            if translation in self.tree[word].translates:
                raise ValueError("Existing translation")
            self.tree[word].translates.append(translation)
            self.tree[word].popularity += 1
        else:
            raise ValueError("Word doesn't exist")

    def change_translation(self, word, translation, new_translation):
        if word in self.tree:
            if translation not in self.tree[word].translates:
                raise ValueError("Translation not found")
            for index, value in enumerate(self.tree[word].translates):
                if value == translation:
                    self.tree[word].translates[index] = new_translation
                    self.tree[word].popularity += 1
        else:
            raise ValueError("Word doesn't exist")

    def delete_translation(self, word, translation):
        if word in self.tree:
            if translation not in self.tree[word].translates:
                raise ValueError("Translation not found")
            if translation in self.tree[word].translates:
                self.tree[word].translates.remove(translation)
                self.tree[word].popularity += 1
        else:
            raise ValueError("Word doesn't exist")

    def display(self):
        if len(self.tree) > 0:
            for word in self.tree.values():
                print(word)
        else:
            raise IndexError("Tree is empty")

    def search(self, word):
        if word in self.tree:
            self.tree[word].popularity += 1
            return self.tree[word]
        else:
            raise ValueError("Word doesn't exist")

    def count(self):
        return len(self.tree)

    def lowest_popularity(self):
        words = self.tree.values()
        popularity = []
        for word in words:
            popularity.append((word, word.popularity))
        min_popularity = min(popularity, key=lambda x: x[1])
        return min_popularity[0]

    def max_popularity(self):
        words = self.tree.values()
        popularity = []
        for word in words:
            popularity.append((word, word.popularity))
        max_popularity = max(popularity, key=lambda x: x[1])
        return max_popularity[0]


try:
    dictionary = Dictionary()
    print("Adding new words: ")
    dictionary.insert_word("apple")
    dictionary.insert_word("morning")
    dictionary.insert_word("cat")
    # dictionary.insert_word("cat")
    dictionary.display()

    print("Dictionary after deletion: ")
    dictionary.delete_word("cat")
    # dictionary.delete_word("cat")
    dictionary.display()

    print("Update word: ")
    dictionary.update_word("apple", "cat")
    # dictionary.update_word("banana", "cat")
    dictionary.display()

    print("Adding translation: ")
    dictionary.add_translation("cat", "кіт")
    dictionary.add_translation("cat", "кошеня")
    # dictionary.add_translation("cat", "кошеня")
    dictionary.add_translation("morning", "ранок")
    dictionary.add_translation("morning", "раночок")
    dictionary.add_translation("morning", "ранок4")
    dictionary.display()

    print("Changing translation: ")
    dictionary.change_translation("morning", "ранок", "ранок2")
    # dictionary.change_translation("morning", "ранок", "ранок2")
    dictionary.display()

    print("Delete translation: ")
    dictionary.delete_translation("morning", "ранок2")
    # dictionary.delete_translation("morning", "ранок3")
    dictionary.display()
    print("Min popularity: " , dictionary.lowest_popularity())
    print("Max popularity: ", dictionary.max_popularity())
    print("Search: ", dictionary.search("cat"))
except ValueError as e:
    print("Message: ", e)
except IndexError as e:
    print("Message: ", e)
except Exception as e:
    print("Message: ", e)

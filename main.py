# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None
#
#     def insert(self, data):
#         if self.root is None:
#             self.root = Node(data)
#         else:
#             self._recursive_insert(data, self.root)
#
#     def _recursive_insert(self, data, current_node):
#         if data < current_node.data:
#             if current_node.left is None:
#                 current_node.left = Node(data)
#             else:
#                 self._recursive_insert(data, current_node.left)
#         else:
#             if current_node.right is None:
#                 current_node.right = Node(data)
#             else:
#                 self._recursive_insert(data, current_node.right)
#
#     def min(self):
#         if self.root is None:
#             print("Tree is empty")
#             return
#         node = self.root
#
#         while node.left is not None:
#             node = node.left
#
#         return node.data
#
#     def max(self):
#         if self.root is None:
#             print("Tree is empty")
#             return
#         node = self.root
#
#         while node.right is not None:
#             node = node.right
#
#         return node.data
#
#     def __contains__(self, data):
#         if self.root is None:
#             print("Tree is empty")
#             return
#         node = self.root
#
#         while node:
#             if node.data == data:
#                 return True
#             if data < node.data:
#                 node = node.left
#             else:
#                 node = node.right
#         return False
#
#     def print(self):
#         if self.root is None:
#             print("Tree is empty")
#             return
#
#         self._inoder(self.root)
#         print()
#
#     def _inoder(self, node):
#         if node is not None:
#             self._inoder(node.left)
#             print(node.data, end=' ')
#             self._inoder(node.right)
#
#     def _preoder(self, node):
#         if node is not None:
#             print(node.data, end=' ')
#             self._preoder(node.left)
#             self._preoder(node.right)
#
#     def _postoder(self, node):
#         if node is not None:
#             self._postoder(node.left)
#             self._postoder(node.right)
#             print(node.data, end=' ')
#
#
# tree = BinaryTree()
# tree.insert(3)
# tree.insert(2)
# tree.insert(4)
# tree.insert(9)
# tree.insert(7)
# tree.insert(6)
# print(tree.min())
# print(tree.max())
# print(4 in tree)
# print(8 in tree)
# tree.print()

import bintrees


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title}, {self.author}, {self.year}"


class Library:
    def __init__(self):
        self.tree = bintrees.AVLTree()

    def insert(self, title, author, year):
        book = Book(title, author, year)
        self.tree.insert(key=title, value=book)

    def search(self, title):
        if title in self.tree:
            return self.tree[title]
        else:
            print("Book doesn't exist")

    def delete(self, title):
        if title in self.tree:
            self.tree.remove(title)
        else:
            print("Book doesn't exist")

    def display(self):
        for book in self.tree.values():
            print(book)

    def count(self):
        return len(self.tree)


library = Library()

library.insert("1984", "George Orwell", 1949)
library.insert("To Kill a Mockingbird", "Harper Lee", 1960)
library.insert("Pride and Prejudice", "Jane Austen", 1813)

print("Books in library:")
library.display()

print("\nSearching for '1984':")
book = library.search("1984")
print(book)

library.delete("To Kill a Mockingbird")
print("\nBooks in library after deletion:")
library.display()

print("\nTotal number of books:", library.count())


class WordNode:
    def __init__(self, word, translate):
        self.word = 'ябко'
        self.translate = {'apple'}
        self.popularity = 0
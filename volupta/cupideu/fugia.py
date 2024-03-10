# To sort a list of numbers in ascending order
numbers = [5, 2, 9, 7, 1]
sorted_numbers = sorted(numbers) # returns a new sorted list
numbers.sort() # modifies the original list in place

# To sort a list of strings in alphabetical order
words = ["apple", "banana", "cherry", "date", "elderberry"]
sorted_words = sorted(words) # returns a new sorted list
words.sort() # modifies the original list in place

# To sort a list of tuples by the second element
pairs = [(1, "a"), (3, "c"), (2, "b"), (4, "d")]
sorted_pairs = sorted(pairs, key=lambda x: x[1]) # returns a new sorted list
pairs.sort(key=lambda x: x[1]) # modifies the original list in place
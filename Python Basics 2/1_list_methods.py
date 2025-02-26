"""
List Methods Covered:
1. append()
2. clear()
3. copy()
4. count()
5. extend()
6. index()
7. insert()
8. pop()
9. remove()
10. reverse()
11. sort()
"""


def demo_append():
    print(">>> DEMO: append() method")
    numbers = [1, 2, 3]
    print("Initial list:", numbers)
    # Expected: [1, 2, 3]
    numbers.append(4)
    print("After append(4):", numbers)
    # Expected: [1, 2, 3, 4]
    print()


def demo_clear():
    print(">>> DEMO: clear() method")
    items = ["apple", "banana", "cherry"]
    print("Initial list:", items)
    # Expected: ["apple", "banana", "cherry"]
    items.clear()
    print("After clear():", items)
    # Expected: []
    print()


def demo_copy():
    print(">>> DEMO: copy() method")
    original = [1, 2, 3]
    copied = original.copy()
    print("Original list:", original)
    # Expected: [1, 2, 3]
    print("Copied list:", copied)
    # Expected: [1, 2, 3]
    # Modify original to show that it's a shallow copy
    original.append(4)
    print("After original.append(4):")
    print("Modified Original list:", original)
    # Expected: [1, 2, 3, 4]
    print("Copied list remains unchanged:", copied)
    # Expected: [1, 2, 3]
    print()


def demo_count():
    print(">>> DEMO: count() method")
    letters = ["a", "b", "c", "a", "a"]
    print("List:", letters)
    # Expected: ['a', 'b', 'c', 'a', 'a']
    count_a = letters.count("a")
    count_b = letters.count("b")
    print("Count of 'a':", count_a)
    # Expected: 3
    print("Count of 'b':", count_b)
    # Expected: 1
    print()


def demo_extend():
    print(">>> DEMO: extend() method")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    print("List1:", list1)
    # Expected: [1, 2, 3]
    print("List2:", list2)
    # Expected: [4, 5, 6]
    list1.extend(list2)
    print("After extend(list2):", list1)
    # Expected: [1, 2, 3, 4, 5, 6]
    print()


def demo_index():
    print(">>> DEMO: index() method")
    fruits = ["apple", "banana", "cherry", "date", "apple"]
    print("List:", fruits)
    # Expected: ["apple", "banana", "cherry", "date", "apple"]
    index_banana = fruits.index("banana")
    index_apple = fruits.index("apple")  # Returns the first occurrence.
    print("Index of 'banana':", index_banana)
    # Expected: 1
    print("Index of 'apple':", index_apple)
    # Expected: 0
    print()


def demo_insert():
    print(">>> DEMO: insert() method")
    nums = [10, 20, 30]
    print("Initial list:", nums)
    # Expected: [10, 20, 30]
    nums.insert(1, 15)  # Insert 15 at index 1.
    print("After insert(1, 15):", nums)
    # Expected: [10, 15, 20, 30]
    print()


def demo_pop():
    print(">>> DEMO: pop() method")
    elems = ["a", "b", "c", "d"]
    print("Initial list:", elems)
    # Expected: ['a', 'b', 'c', 'd']
    popped_item = elems.pop()  # Removes the last element.
    print("Popped item:", popped_item)
    # Expected: 'd'
    print("After pop():", elems)
    # Expected: ['a', 'b', 'c']
    popped_index_item = elems.pop(1)  # Removes element at index 1.
    print("Popped element at index 1:", popped_index_item)
    # Expected: 'b'
    print("After second pop():", elems)
    # Expected: ['a', 'c']
    print()


def demo_remove():
    print(">>> DEMO: remove() method")
    numbers = [1, 2, 3, 2, 4]
    print("Initial list:", numbers)
    # Expected: [1, 2, 3, 2, 4]
    numbers.remove(2)  # Removes the first occurrence of 2.
    print("After remove(2):", numbers)
    # Expected: [1, 3, 2, 4]
    print()


def demo_reverse():
    print(">>> DEMO: reverse() method")
    data = [1, 2, 3, 4, 5]
    print("Initial list:", data)
    # Expected: [1, 2, 3, 4, 5]
    data.reverse()
    print("After reverse():", data)
    # Expected: [5, 4, 3, 2, 1]
    print()


def demo_sort():
    print(">>> DEMO: sort() method")
    fruits = ["banana", "apple", "cherry", "date"]
    print("Unsorted list:", fruits)
    # Expected: ["banana", "apple", "cherry", "date"]
    fruits.sort()
    print("After sort():", fruits)
    # Expected: ['apple', 'banana', 'cherry', 'date']

    # Example with a key function (sort by length)
    fruits = ["kiwi", "pineapple", "fig", "grape"]
    print("\nUnsorted list:", fruits)
    # Expected: ["kiwi", "pineapple", "fig", "grape"]
    fruits.sort(key=len)
    print("After sort(key=len):", fruits)
    # Expected: ['fig', 'kiwi', 'grape', 'pineapple']
    print()


def main():
    print("Python List Methods Learning Module Demonstration")
    print("--------------------------------------------------\n")
    demo_append()
    demo_clear()
    demo_copy()
    demo_count()
    demo_extend()
    demo_index()
    demo_insert()
    demo_pop()
    demo_remove()
    demo_reverse()
    demo_sort()


if __name__ == "__main__":
    main()

# advanced_main.py
# Advanced Python Collections Demonstration
# -----------------------------------------------
# Covers lists, tuples, sets, dictionaries with slicing,
# comprehensions, copying, nested collections, unpacking, and more.

import copy

def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ===================== 1. LIST =====================
def demonstrate_advanced_list():
    print_section("1. LIST (Ordered, Mutable, Duplicates Allowed)")

    fruits = ["apple", "banana", "mango", "banana", "orange"]
    print("Original list:", fruits)

    # Slicing
    print("First three items:", fruits[:3])
    print("Every second item:", fruits[::2])
    print("Reversed list:", fruits[::-1])

    # List comprehensions
    upper_fruits = [f.upper() for f in fruits]
    print("Uppercase list (comprehension):", upper_fruits)

    # Conditional comprehension
    unique_fruits = [f for f in fruits if f != "banana"]
    print("List without 'banana':", unique_fruits)

    # Enumerate
    print("Enumerate with index:")
    for idx, fruit in enumerate(fruits):
        print(f"{idx}: {fruit}")

    # Copying
    list_copy = fruits.copy()        # Shallow copy
    list_reference = fruits          # Reference (not copy)
    fruits.append("grape")
    print("Original after append:", fruits)
    print("Shallow copy (unchanged):", list_copy)
    print("Reference points to same object:", list_reference)

    # Nested list
    nested = [[1, 2], [3, 4], [5, 6]]
    print("Nested list:", nested)
    print("Access nested element [1][0]:", nested[1][0])


# ===================== 2. TUPLE =====================
def demonstrate_advanced_tuple():
    print_section("2. TUPLE (Ordered, Immutable, Duplicates Allowed)")

    coords = (10, 20, 30, 20)
    print("Tuple:", coords)

    # Slicing
    print("Slice coords[1:3]:", coords[1:3])
    print("Reversed tuple:", coords[::-1])

    # Unpacking
    x, y, z, _ = coords
    print(f"Unpacked: x={x}, y={y}, z={z}")

    # Nested tuple
    nested_tuple = ((1, 2), (3, 4))
    print("Nested tuple:", nested_tuple)
    print("Access nested [1][0]:", nested_tuple[1][0])


# ===================== 3. SET =====================
def demonstrate_advanced_set():
    print_section("3. SET (Unordered, Mutable, Unique Elements)")

    numbers = {1, 2, 3, 2, 1}
    print("Original set (duplicates removed):", numbers)

    # Adding/removing
    numbers.add(4)
    numbers.discard(5)  # No error if not present
    print("After add/discard:", numbers)

    # Set operations
    other_set = {3, 4, 5}
    print("Union:", numbers | other_set)
    print("Intersection:", numbers & other_set)
    print("Difference:", numbers - other_set)
    print("Symmetric difference:", numbers ^ other_set)

    # Set comprehension
    squared = {x**2 for x in range(5)}
    print("Squared set (comprehension):", squared)


# ===================== 4. DICTIONARY =====================
def demonstrate_advanced_dict():
    print_section("4. DICTIONARY (Key-Value Pairs, Mutable, Ordered)")

    person = {"name": "Kelvin", "age": 22, "country": "Rwanda"}
    print("Original dict:", person)

    # Access / update
    person["age"] = 23
    person["profession"] = "Developer"

    # Iteration
    print("Keys and values:")
    for k, v in person.items():
        print(f"{k}: {v}")

    # Dictionary comprehension
    squared_dict = {x: x**2 for x in range(5)}
    print("Squared dictionary (comprehension):", squared_dict)

    # Nested dictionary
    nested_dict = {"person1": {"name": "Aime", "age": 25},
                   "person2": {"name": "Kelvin", "age": 22}}
    print("Nested dict:", nested_dict)
    print("Access nested person2 age:", nested_dict["person2"]["age"])

    # Unpacking keys and values
    keys = [*person]
    values = [*person.values()]
    print("Keys unpacked:", keys)
    print("Values unpacked:", values)


# ===================== 5. STRING ADVANCED =====================
def demonstrate_string_operations():
    print_section("5. STRING (Ordered, Immutable)")

    text = "Python"
    print("Original string:", text)

    # Slicing
    print("Slice text[1:4]:", text[1:4])
    print("Reversed text:", text[::-1])

    # Comprehension
    vowels = [c for c in text if c.lower() in "aeiou"]
    print("Vowels in text:", vowels)


# ===================== 6. ZIP, ENUMERATE, UNPACKING =====================
def demonstrate_iteration_tools():
    print_section("6. ZIP, ENUMERATE, UNPACKING")

    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]

    # Zip
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

    # Enumerate
    for idx, name in enumerate(names, start=1):
        print(f"{idx}. {name}")

    # Multiple unpacking
    a, *middle, c = [1, 2, 3, 4, 5]
    print("Multiple unpacking:", a, middle, c)


# ===================== 7. COPY AND MUTABILITY =====================
def demonstrate_copying():
    print_section("7. COPY & MUTABILITY")

    original_list = [[1, 2], [3, 4]]
    shallow = copy.copy(original_list)
    deep = copy.deepcopy(original_list)

    # Modify nested
    original_list[0][0] = 99
    print("Original list modified:", original_list)
    print("Shallow copy affected:", shallow)
    print("Deep copy unaffected:", deep)


# ===================== 8. SORTING WITH LAMBDA =====================
def demonstrate_sorting_lambda():
    print_section("8. SORTING & LAMBDA")

    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 30}
    ]

    # Sort by age ascending
    sorted_people = sorted(people, key=lambda x: x["age"])
    print("Sorted by age:", sorted_people)

    # Sort by name descending
    sorted_by_name = sorted(people, key=lambda x: x["name"], reverse=True)
    print("Sorted by name descending:", sorted_by_name)


# ===================== MAIN =====================
def main():
    print_section("ADVANCED PYTHON COLLECTIONS DEMO")

    demonstrate_advanced_list()
    demonstrate_advanced_tuple()
    demonstrate_advanced_set()
    demonstrate_advanced_dict()
    demonstrate_string_operations()
    demonstrate_iteration_tools()
    demonstrate_copying()
    demonstrate_sorting_lambda()

    print("\nAdvanced Python Collections Demonstration Completed Successfully.")


if __name__ == "__main__":
    main()

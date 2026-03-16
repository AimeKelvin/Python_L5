# Comprehensive Demonstration of Python Collections
def print_section(title):
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)


def demonstrate_list():
    print_section("1. LIST (Ordered, Mutable, Allows Duplicates)")

    # Creating a list
    fruits = ["apple", "banana", "mango", "banana"]
    print("Original List:", fruits)

    # Accessing elements
    print("First item:", fruits[0])
    print("Last item:", fruits[-1])

    # Adding elements
    fruits.append("orange")
    print("After append:", fruits)

    fruits.insert(1, "grape")
    print("After insert at index 1:", fruits)

    # Removing elements
    fruits.remove("banana")  # removes first occurrence
    print("After remove:", fruits)

    popped_item = fruits.pop()
    print("Popped item:", popped_item)
    print("After pop:", fruits)

    # Sorting
    fruits.sort()
    print("Sorted list:", fruits)

    # Looping
    print("Looping through list:")
    for fruit in fruits:
        print("-", fruit)

    # Checking type
    print("Type:", type(fruits))


def demonstrate_tuple():
    print_section("2. TUPLE (Ordered, Immutable, Allows Duplicates)")

    coordinates = (10, 20, 30, 20)
    print("Tuple:", coordinates)

    # Accessing
    print("First value:", coordinates[0])

    # Count and index methods
    print("Count of 20:", coordinates.count(20))
    print("Index of 30:", coordinates.index(30))

    # Attempting modification (will cause error if uncommented)
    # coordinates[0] = 50  # Tuples are immutable

    print("Tuples cannot be modified after creation.")

    print("Looping through tuple:")
    for value in coordinates:
        print("-", value)

    print("Type:", type(coordinates))


def demonstrate_set():
    print_section("3. SET (Unordered, Mutable, No Duplicates)")

    numbers = {1, 2, 3, 2, 1}
    print("Set (duplicates removed automatically):", numbers)

    # Adding elements
    numbers.add(4)
    print("After add:", numbers)

    # Removing elements
    numbers.remove(3)
    print("After remove:", numbers)

    # Set operations
    other_set = {3, 4, 5}

    print("Union:", numbers.union(other_set))
    print("Intersection:", numbers.intersection(other_set))
    print("Difference:", numbers.difference(other_set))

    print("Looping through set:")
    for num in numbers:
        print("-", num)

    print("Type:", type(numbers))


def demonstrate_dictionary():
    print_section("4. DICTIONARY (Key-Value Pairs, Mutable, Unique Keys)")

    person = {
        "name": "Kelvin",
        "age": 22,
        "country": "Rwanda"
    }

    print("Dictionary:", person)

    # Accessing values
    print("Name:", person["name"])

    # Adding / Updating
    person["profession"] = "Developer"
    print("After adding profession:", person)

    person["age"] = 23
    print("After updating age:", person)

    # Removing
    removed_value = person.pop("country")
    print("Removed country:", removed_value)
    print("After pop:", person)

    # Looping
    print("Looping through dictionary (keys):")
    for key in person:
        print("-", key)

    print("Looping through dictionary (key-value pairs):")
    for key, value in person.items():
        print(f"{key} : {value}")

    print("Keys:", person.keys())
    print("Values:", person.values())

    print("Type:", type(person))


def demonstrate_common_operations():
    print_section("5. COMMON COLLECTION OPERATIONS")

    sample_list = [1, 2, 3, 4]

    # Length
    print("Length:", len(sample_list))

    # Membership
    print("Is 3 in list?", 3 in sample_list)

    # Type checking
    print("Is sample_list a list?", isinstance(sample_list, list))

    # Converting between collections
    tuple_version = tuple(sample_list)
    set_version = set(sample_list)

    print("Converted to tuple:", tuple_version)
    print("Converted to set:", set_version)


def main():
    print_section("PYTHON COLLECTIONS FULL DEMONSTRATION")

    demonstrate_list()
    demonstrate_tuple()
    demonstrate_set()
    demonstrate_dictionary()
    demonstrate_common_operations()

    print("\nProgram Completed Successfully.")


if __name__ == "__main__":
    main()

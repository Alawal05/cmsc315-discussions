"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # The insert method adds the value at tge specified position.
    # Existing items at that position and after it shift to the right.
    # Inserting at the beginning or middle may take more time because
    # more items have to move compared to inserting at the end.
    lst.insert(index, value)
    


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Checks the index before deleting to avoid an error.
    if 0 <= index < len(lst):
        # Pop removes the item and returns the removed value.
        return lst.pop(index)
    # If the index does not exist, return None.
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # A linear search checks each item one at a tome.
    # It starts from the beginning until the value is found.
    for index, item in enumerate(lst):
        if item == value:
            return index
        # Return -1 if the value is not in the list.
        return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
   
    contacts = ["Amir", "Sarah", "John", "Mary"]
    print("Original contacts:", contacts)

    #Add a new contact at the beginning.
    insert_at(contacts, 0, "Amina")
    print("After beginning insertion:", contacts)

    # Add a contact in the middle.
    insert_at(contacts, 2, "David")
    print("After middle insertion:", contacts)

    # Add a contact ag the end.
    insert_at(contacts, len(contacts), "Grace")
    print("After end insertion:", contacts)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
   
    # Remove the first contact from the list.
    removed = delete_at(contacts, 0)
    print("Removed from beginning:", removed)
    print("Updated contacts:", contacts)

    # Remove a contact from the middle.
    removed = delete_at(contacts, len(contacts) // 2)
    print("Removed from middle:", removed)
    print("Updated contacts:", contacts)

    # Remove the last contact from the list.
    removed = delete_at(contacts, len(contacts) -1)
    print("Removed from end:", removed)
    print("Updated contacts:", contacts)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
  
    # Search for a contact that is in the list.
    position = search_value(contacts, "Sarah")
    print("Sarah was found at index:", position)

    # Search for a contact that is not in the list.
    position = search_value(contacts, "Michael")
    print("Michale search result:", position)
    print("-1 means the contact was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    
    # Test deleting from an empty list.
    empty_contacts = []
    removed = delete_at(empty_contacts, 0)
    print("Deleting from an empty list:", removed)

    # Test deleting using an invalid index.
    removed = delete_at(contacts, 100)
    print("Deleting at invalid index:", removed)

    # Test inserting into an empty list.
    insert_at(empty_contacts, 0, "Blessing")
    print("Inserting into an empty listt:", empty_contacts)

    # Test searching for a contact that is missing.
    position = search_value(contacts, "Unknown")
    print("Searching for a missing contacts:", position)



if __name__ == "__main__":
    main()

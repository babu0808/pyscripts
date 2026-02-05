def transform_input(strings):
    """
    Transforms each string to uppercase and appends '_H'.

    Args:
        strings (list of str): List of input strings.

    Returns:
        list of str: Transformed strings.
    """
    return [string.upper() + "_H" for string in strings]

if __name__ == "__main__":
    print("Enter strings one by one (press Enter after each string, type 'done' to finish):")
    input_strings = []
    
    while True:
        user_input = input().strip()
        if user_input.lower() == "done":
            break
        input_strings.append(user_input)
    
    transformed_strings = transform_input(input_strings)
    
    print("\nTransformed strings:")
    for transformed_string in transformed_strings:
        print(transformed_string)

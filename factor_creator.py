def split_fraction(fraction: str) -> list:
    split = [int(num) for num in fraction.split("/")]
    if len(split) < 2:
        split.append(1)

    return split


def get_input():
    # Get user input
    numbers = input("Please enter numbers: ").split()
    numerators = []
    denominators = []

    for item in numbers:
        # Separate numerators from denominators
        split_fractions = split_fraction(item)
        numerators.append(split_fractions[0])
        denominators.append(split_fractions[1])

    return numerators, denominators


def create_factors(*numbers: int) -> dict:
    factors = {}
    for number in numbers:
        low_end = []
        high_end = []

        # Create both ends of the list
        for i in range(1, 11):
            remainder = number % i
            if remainder == 0:
                low_end.append(i)
                high_end.append(number // i)

        # Add the two lists
        factors[number] = low_end[:-1] + high_end[-2::-1]

    return factors


def get_least_common_denom(numerators: list, *denominators: str) -> int:
    multiple = 1
    lcd = 1  # Least common denominator
    found = False
    denominators = sorted(denominators)[::-1]
    while not found:

        index = 0
        if len(denominators) == 1:
            # Return the number itself
            return int(denominators[0])

        for num in denominators[1:]:
            # Cycle through all numbers in the list provided, except the first.
            lcd = denominators[0] * multiple
            if lcd % num != 0:
                # The resulting number doesn't divide into the other numbers
                found = False
                index += 1
                break

            found = True

        multiple += 1

    return lcd


def convert_list(numerators: list,
                 denom: list,
                 lcd: int,
                 ) -> list:
    return_list = []
    index = 0
    multiple = 1

    for num in numerators:
        # The multiple is the number to multiply the denominator by to reach
        # the least common denominator
        multiple = lcd // denom[index]
        multiplied_numerator = str(num * multiple)

        return_list.append("/".join(
            [multiplied_numerator, str(lcd)]
        ))

        index += 1

    return [return_list, multiple]


if __name__ == "__main__":
    # Get numerators and denominators into their own lists
    numer, denom = get_input()

    # Get the least common denominator
    lcd = get_least_common_denom(numer, *denom)

    # Get the factors of each number
    denom_factors = create_factors(*denom)
    numer_factors = create_factors(*numer)

    # Multiply all factors by the least common denominator
    converted_list, multiple = convert_list(numer, denom, lcd)

    # Print the results
    for k, v in denom_factors.items():
        print(f"Denominator: {k:03}, Length: {len(v):03}, Factors: {v}")

    for k, v in numer_factors.items():
        print(f"Numerator: {k:03}, Length: {len(v):03}, Factors: {v}")

    print(f"Least Common Denominator: {lcd}")
    print("Converted Factors: ", end='')
    print(*converted_list, sep=" | ")

    # Add all numerators for final answer
    final_result = 0
    for fraction in converted_list:
        final_result += int(fraction.split("/")[0])

    # Print final answer
    print(f"Improper Fraction: {final_result}/{lcd}")

    # Get mixed number
    remainder = final_result % lcd
    mixed_number = final_result // lcd

    # Print mixed number
    print(f"Mixed number: {mixed_number} {remainder}/{lcd}")

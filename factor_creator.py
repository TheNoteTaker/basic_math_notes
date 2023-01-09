import sys

def split_fraction(fraction: str) -> list:
    split = [int(num) for num in fraction.split("/")]
    if len(split) < 2:
        split.append(1)

    return split


def get_input():
    numerators = []
    denominators = []

    if len(sys.argv) < 2:
        print("No arguments were provided! Please run again and provide some.")
        exit(1)

    for item in sys.argv[1:]:
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
        factors[number] = sorted(set(low_end + high_end))

    return factors


def get_least_common_multiple(*number_list: str) -> int:
    multiple = 1
    lcd = 1  # Least common denominator
    found = False
    number_list = sorted(number_list)[::-1]
    while not found:

        index = 0
        if len(number_list) == 1:
            # Return the number itself
            return int(number_list[0])

        for num in number_list[1:]:
            # Cycle through all numbers in the list provided, except the first.
            lcd = number_list[0] * multiple
            if lcd % num != 0:
                # The resulting number doesn't divide into the other numbers
                found = False
                index += 1
                break

            found = True

        multiple += 1

    return lcd


def get_greatest_common_factor(factors_list) -> int:
    iterator_set = set()
    for number_set in factors_list:
        if iterator_set:
            iterator_set = iterator_set.intersection(number_set)
        else:
            iterator_set = set(number_set)

    # Now contains only factors that are shared between all factor lists, so
    # return the highest one.
    return max(iterator_set)


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
    lcd = get_least_common_multiple(*denom)
    lcn = get_least_common_multiple(*numer)

    # Get the factors of each number
    denom_factors = create_factors(*denom)
    numer_factors = create_factors(*numer)

    # Multiply all factors by the least common denominator
    converted_list, multiple = convert_list(numer, denom, lcd)

    # Print the numerator factors
    for k, v in numer_factors.items():
        # # Store length for future use
        # length_of_list = len(v)
        numer_prime_factors = []
        # if length_of_list % 2 == 1:
        #     # There is a prime factor if there's an odd number left
        #     numer_prime_factors.append(v)

        print(f"Numerator: {k:03}, Length: {len(v):03}, Factors: {v}")
        # if numer_prime_factors:
        #     print(f"Prime Factors: {numer_prime_factors}")

    # Print the denominator factors
    for k, v in denom_factors.items():
        # # Store length for future use
        # length_of_list = len(v)
        # denom_prime_factors = []
        # if length_of_list % 2 == 1:
        #     # There is a prime factor if there's an odd number left
        #     denom_prime_factors.append(v)

        print(f"Denominator: {k:03}, Length: {len(v):03}, Factors: {v}")
        # if denom_prime_factors:
        #     print(f"Prime Factors: {denom_prime_factors}")

    # Get the Greatest Common Factor for denominator
    greatest_factor_denominator = get_greatest_common_factor(
        denom_factors.values()
    )

    # Get the Greatest Common Factor for numerator
    greatest_factor_numerator = get_greatest_common_factor(
        numer_factors.values()
    )

    print(f"Greatest Common Factor (Num): {greatest_factor_numerator}")
    print(f"Greatest Common Factor (Denom): {greatest_factor_denominator}")
    print(f"Least Common Numerator: {lcn}")
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
    if remainder:
        print(f"Mixed number: {mixed_number} {remainder}/{lcd}")
    else:
        print(f"Mixed number: {mixed_number}")

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2 == 1

def steps(number: int) -> bool:
    try:
        if number <= 0:
            raise ValueError("Only positive integers are allowed")
        else:
            steps = 0
            while number != 1:
                if is_even(number):
                    number /= 2
                    steps += 1
                elif is_odd(number):
                    number *= 3
                    number += 1
                    steps += 1
            return steps

    except ValueError as e:
        print(f"Error: {e}")
        raise
print(steps(12))
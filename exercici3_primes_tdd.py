import unittest

def get_primes_up_to(limit):
    if limit < 2:
        return []
    
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(num)
            
    return primes

class TestPrimeGenerator(unittest.TestCase):
    
    def test_limit_less_than_two_returns_empty(self):
        self.assertEqual(get_primes_up_to(0), [])
        self.assertEqual(get_primes_up_to(1), [])

    def test_primes_up_to_two(self):
        self.assertEqual(get_primes_up_to(2), [2])

    def test_primes_up_to_ten(self):
        self.assertEqual(get_primes_up_to(10), [2, 3, 5, 7])
        
    def test_primes_up_to_twenty(self):
        expected_primes = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(get_primes_up_to(20), expected_primes)

if __name__ == "__main__":
    unittest.main(exit=False)
    print("\n--- Prime Number Generator ---")
    try:
        user_input = int(input("Enter a limit to calculate prime numbers: "))
        result = get_primes_up_to(user_input)
        print(f"Prime numbers up to {user_input}: {result}")
    except ValueError:
        print("Please enter a valid integer.")
class DFA_Modulus:
    def __init__(self, divisor):
        self.divisor = divisor
        self.states = list(range(divisor))  # states = 0 to divisor-1
        self.start_state = 0
    def transition(self, current_state, bit):
        return (2 * current_state + int(bit)) % self.divisor
    def compute_remainder(self, binary_string):
        current_state = self.start_state
        print(f"Start State: {current_state}")
        for bit in binary_string:
            current_state = self.transition(current_state, bit)
            print(f"After reading '{bit}' → State: {current_state}")
        return current_state
#MAIN PROGRAM 
binary_input = input("Enter a binary number: ")
divisor = int(input("Enter divisor: "))
dfa = DFA_Modulus(divisor)
remainder = dfa.compute_remainder(binary_input)
print("\nFinal Remainder:", remainder)
if remainder == 0:
    print("The number is divisible by", divisor)
else:
    print("The number is NOT divisible by", divisor)

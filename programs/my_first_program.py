

from nada_dsl import Party, SecretInteger, Input, Output

def nada_main():
    # Define the party involved
    party1 = Party(name="Party1")

    # Input secret integers from party1
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))

    # Compute the sum of the inputs
    sum_result = my_int1 + my_int2

    # Compute the product of the inputs
    product_result = my_int1 * my_int2

    # Compute the difference of the inputs
    difference_result = my_int1 - my_int2

    # Check if the first integer is greater than the second
    comparison_result = my_int1 > my_int2

    # Create a detailed output with multiple results
    outputs = [
        Output(sum_result, "sum_result", party1),
        Output(product_result, "product_result", party1),
        Output(difference_result, "difference_result", party1),
        Output(comparison_result, "comparison_result", party1)
    ]

    return outputs

# Create the NADA program
if __name__ == "__main__":
    outputs = nada_main()
    for output in outputs:
        print(output)
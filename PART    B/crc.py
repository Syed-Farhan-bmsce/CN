def crc(ip, poly, mode):
    # Convert input to a mutable list for bitwise operations
    op = list(ip)

    if mode:
        # Append zeros to the message based on the length of the polynomial
        op.extend(['0'] * (len(poly) - 1))

    # Perform division
    for i in range(len(op) - len(poly) + 1):
        if op[i] == '1':
            for j in range(len(poly)):
                op[i + j] = '0' if op[i + j] == poly[j] else '1'

    # Return the modified output
    return ''.join(op)


def main():
    # Example CRC-8 polynomial
    poly = "100000111"

    # Input message
    ip = input("Enter the input message: ")

    # Compute transmitted message
    remainder = crc(ip, poly, mode=1)[len(ip):]
    transmitted_message = ip + remainder
    print(f"Transmitted message: {transmitted_message}")

    # Simulate received message
    recv = input("Enter received message: ")

    # Check for errors
    check_result = crc(recv, poly, mode=0)
    if all(bit == '0' for bit in check_result[len(recv) - len(poly) + 1:]):
        print("No error in data transmission")
    else:
        print("Error in data transmission")


if name == "main":
    main()

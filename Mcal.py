# arr = [101*12, 62*11, 60*11.50, 60*11, 80*11, 60*11, 63*11, 60*11]
# sum = 0
# print(arr)
# for item in arr:
#     sum += item
# print (sum)

# Import required module
import sys

# Initialize total sum
sum_total = 0

# Take input in "piece-price" format
input_str = input("Enter pice * price (format: 11-22,30-10,60-11): ")

# Split the input by commas
pairs = input_str.split(',')

# Process each pair
for pair in pairs:
    try:
        # Split each pair by '-' and convert to float
        piece_str, price_str = pair.strip().split('-')
        piece = float(piece_str)
        price = float(price_str)

        # Calculate total for the pair
        total = piece * price
        print(f"{piece} x {price} = {total}")
        sum_total += total
    except ValueError:
        print(f"Invalid pair skipped: {pair}")

# Final result
print(f"\nFinal Total Cost: {sum_total}")



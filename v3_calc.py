import time

# Ask for the length of the vanity address
address_length = int(input("How long is the Tor v3 vanity address? "))

# Ask for the number of calculations per second
calculations_per_second = int(input("How many calculations per second can your CPU do? "))

# Calculate the number of seconds required to generate the address
seconds_required = 32 ** address_length / calculations_per_second

# Convert the seconds to days, hours, and minutes
minutes, seconds = divmod(seconds_required, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)

# Display the result to the user
print(f"It would take {days} days, {hours} hours, and {minutes} minutes to generate a v3 vanity address of length {address_length} at {calculations_per_second} calculations per second.")

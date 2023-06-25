import sys

# Retrieve the command-line arguments
argv = sys.argv[1:]

# Get the number of arguments
num_args = len(argv)

# Print the number of arguments
print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}{'.' if num_args == 0 else ':'}")

# Print each argument
for i, arg in enumerate(argv, 1):
    print(f"{i}: {arg}")

import re

# Path to the HQL file
file_path = '/data/duniy/case_state.hql'

# Read the contents of the file
with open(file_path, 'r') as file:
    hql_code = file.read()

# Define the regular expression to find keys for value 1002 (without assuming 'alt_key' suffix)
pattern = r'when [^\n]*?then 1002 end as (\w+[_\w]*)'

# Find all matching keys
keys_1002 = re.findall(pattern, hql_code)

# Print the result
print(keys_1002)

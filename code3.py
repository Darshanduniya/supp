import re

# Read the contents of the HQL file
file_path = '/data/duni/code.hql'
with open(file_path, 'r') as file:
    hql_content = file.read()

# Define the search pattern for the create table and the target lines
search_pattern = r'create table \${SCHEMA_NAME}\.supprsn_stage_final using orc as'

# Find the position of the create table statement
start_index = hql_content.find(search_pattern)

# If the create table statement is found
if start_index != -1:
    # Extract the portion of the file up to the create table statement
    relevant_content = hql_content[:start_index]
    
    # Search for the `from ${SCHEMA_NAME}.supprsn_stage_ref f;` line
    match = re.search(r'from \${SCHEMA_NAME}\.supprsn_stage_ref f;', relevant_content)
    
    # If the match is found, extract the required content
    if match:
        # Extract the select portion of the statement before the 'from'
        select_statement = relevant_content[match.start():]
        
        # Extract only the keys from the select part (between SELECT and FROM)
        select_keys = re.search(r'select(.*?)from', select_statement, re.DOTALL)
        
        if select_keys:
            # Extract the keys, split by commas, and strip any leading/trailing spaces
            keys = [key.strip() for key in select_keys.group(1).split(',')]
            
            # Assign the joined keys to a variable
            keys_string = ', '.join(keys)
            
            # Print the keys string
            print(keys_string)
        else:
            print("No keys found in the select statement.")
    else:
        print("No matching 'from ${SCHEMA_NAME}.supprsn_stage_ref f;' found in the content before the create table statement.")
else:
    print("Create table statement not found in the file.")

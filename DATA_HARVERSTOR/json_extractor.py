import json

# Define the keyword to search for
keyword = "username"

# Create a list to store JSON data
json_data_list = []

# Open the file for reading
with open("m.csv", "r") as file:
    # Read each line in the file
    for line in file:
        # Check if the keyword is present in the line
        if keyword in line:
            # Find and extract JSON data from the line
            start_index = line.find("{")  # Find the first '{' character
            end_index = line.rfind("}")    # Find the last '}' character
            if start_index != -1 and end_index != -1 and end_index > start_index:
                json_data = line[start_index:end_index + 1]
                try:
                    parsed_json = json.loads(json_data)
                    json_data_list.append(parsed_json)
                except json.JSONDecodeError as e:
                    print("Error parsing JSON:", e)

# Sort the list of JSON data based on the 'time' field
sorted_json_data_list = sorted(json_data_list, key=lambda x: x.get('time', 0))

# Open a file for writing the sorted output
with open("sorted_output.txt", "w") as output_file:
    # Write the sorted data to the file
    for data in sorted_json_data_list:
        output_file.write("Time: " + str(data['time']) + "\n")
        output_file.write("IP Address: " + str(data['ip_address']) + "\n")
        output_file.write("Username: " + str(data['post_data']['username']) + "\n")
        output_file.write("Password: " + str(data['post_data']['password']) + "\n")
        output_file.write("=" * 50 + "\n")

print("Sorted output has been written to 'sorted_output.txt'.")

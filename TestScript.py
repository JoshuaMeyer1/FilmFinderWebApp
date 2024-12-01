import pandas as pd

# Load the CSV file into a DataFrame
file_path = "test_data.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Function to get a row by index
def get_row_by_index(index):
    try:
        row = df.iloc[index]  # Get the row by index
        return row.to_dict()["title"]  # Return the row as a dictionary
    except IndexError:
        return f"Index {index} is out of bounds for this CSV file."

# Example usage
#row_index = 34  # Replace with the index of the row you want
#row_data = get_row_by_index(row_index)
#print(row_data)
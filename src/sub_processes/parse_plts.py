import pandas as pd
import re

def parse_plt(file_path):
    # Read the file content
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extract the header with variable names
    header_line = [line for line in lines if line.startswith("VARIABLES")][0]
    pattern = r'"([^"]+)"'
    columns = re.findall(pattern, header_line)
    columns = [col.strip() for col in columns]

    # Filter out data lines (skipping non-data lines like ZONE or metadata)
    data_lines = [
        line for line in lines if not line.startswith(("VARIABLES", "ZONE")) and line.strip()
    ]

    #drop the 3 column data at the end of the plts
    filtered_lines = []
    for line in lines:
        # Split by whitespace
        parts = line.strip().split()
        # Check if this line has only 3 columns
        if len(parts) == 3:
            # We’ve hit the “extra” data; break out and ignore the rest
            break
        filtered_lines.append(line)

    # Filter numerical lines only
    numerical_data_lines = [
        line for line in filtered_lines if all(c.isdigit() or c.isspace() or c in ".-Ee" for c in line)
    ]

    # Adjust the column names to match the number of data entries
    max_columns = max(len(line.split()) for line in numerical_data_lines)
    adjusted_columns = columns[:max_columns] if len(columns) >= max_columns else columns + [f"Extra_{i}" for i in range(max_columns - len(columns))]

    # Create the DataFrame
    data_aligned = pd.DataFrame(
        [list(map(float, line.split())) for line in numerical_data_lines],
        columns=adjusted_columns
    )

    return data_aligned

def main():
    # Define the file path
    file_path = r'C:\Users\RDCRLCSE\Documents\CRISSP2D\StClairRiver\simulations\hy175.5_ice_jam\out/StClair001.plt'

    data_aligned=parse_plt(file_path)

    data_aligned.to_csv('data.csv', index=False)

    # Display the first few rows of the DataFrame
    print(data_aligned.head())

if __name__ == "__main__":
    main()

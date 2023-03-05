import csv
import sys
import os

tags_csv_filename = sys.argv[1]
output_dir = sys.argv[2]
base_tags = sys.argv[3]

def create_tags_txt_file(filename, tags):
    file_path = os.path.join(output_dir, filename + '.txt')

    with open(file_path, 'w') as f:
        # Write the text to the file
        f.write(base_tags + ',' + tags)
    
    print(f'Text file saved to {file_path}')

with open(tags_csv_filename, newline='') as csvfile:
    
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    next(reader)
    
    for row in reader:
        
        # Print the current row
        print(row)
        create_tags_txt_file(row[0], row[1])


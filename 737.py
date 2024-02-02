import os

directory = 'C:/Users/fffff/Downloads/Grand Theft Auto V by Igruha/new_dir'
base_name = 'new_file'
num_digits = 3
original_extension = 'py'
new_extension = 'md'
name_range = (3, 6)

files_to_rename = [f for f in os.listdir(directory) if f.endswith(original_extension)]

for i, file_name in enumerate(files_to_rename):
    if name_range:
        original_name_part = file_name[name_range[0] - 1:name_range[1]]
    else:
        original_name_part = ""

    new_file_name = f"{base_name}_{original_name_part}{str(i + 1).zfill(num_digits)}.{new_extension}"

    original_path = os.path.join(directory, file_name)
    new_path = os.path.join(directory, new_file_name)

    os.rename(original_path, new_path)

    print(f"Renaming: {original_path} to {new_path}")


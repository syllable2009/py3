from pathlib import Path
data_folder = Path("source_data/text_files/")
file_to_open = data_folder / "raw_data.txt"
print(file_to_open.name)
print(file_to_open.suffix)
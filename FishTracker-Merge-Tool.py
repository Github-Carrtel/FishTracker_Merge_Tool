import os
import sys
import csv

# 1. The folder containing the text files is the folder where this program is located.
#    When frozen into a standalone .exe (PyInstaller), use the executable's folder;
#    otherwise use the script's own folder.
if getattr(sys, "frozen", False):
    source_folder = os.path.dirname(os.path.abspath(sys.executable))
else:
    source_folder = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(source_folder, "CSOT_merged.txt")

# 2. Prepare the output; the header (field names) is taken from the first file read.
all_rows = []
fieldnames = None

# 3. Loop through all TXT files in the folder
for file_name in sorted(os.listdir(source_folder)):
    if file_name.endswith("_tracks.txt"):  # Filter: files ending with "tracks.txt"
        file_path = os.path.join(source_folder, file_name)

        # Extract the part of the file name from the 5th to the 15th character for the "Date" column
        Date_str = file_name[5:15]  # Extract characters from index 5 to 14

        # Extract the part of the file name from the 16th to the 22nd character for the "Time" column
        time_str = file_name[16:22]  # Extract characters from index 16 to 21

        # Add ":" between each pair of digits (format 14:05:65)
        if len(time_str) == 6:
            formatted_time = f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:]}"  # e.g. "14:05:65"
        else:
            formatted_time = time_str  # If not in the expected format, leave it as is

        # Read the TXT file with ";" as the separator
        with open(file_path, newline="", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f, delimiter=";")

            # Remember the columns from the first file, then add the three extra columns
            if fieldnames is None:
                fieldnames = list(reader.fieldnames or []) + ["File", "Date", "Time"]

            for row in reader:
                # Add the File / Date / Time columns to each row
                row["File"] = file_name
                row["Date"] = Date_str
                row["Time"] = formatted_time
                all_rows.append(row)

# 4. Save the combined file with ";" as the separator
if all_rows:
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=";", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"Combined file created: {output_file}")
    print(f"{len(all_rows)} rows written.")
else:
    print("No matching files (ending with 'tracks') were found in the folder.")

# Keep the console window open when running as a double-clicked .exe
if getattr(sys, "frozen", False):
    input("\nPress Enter to close...")

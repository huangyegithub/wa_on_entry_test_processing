from OE_Formatter_Rob_Davis import format_school

import os

def main():
    try:
        current_directory = os.getcwd()
        unformatted_directory = os.path.join(current_directory, 'Unformatted')
        school_folders = os.listdir(unformatted_directory)
        school_directories = [os.path.join(unformatted_directory, school_folder) for school_folder in school_folders if os.path.isdir(os.path.join(unformatted_directory, school_folder))]

        for school_directory in school_directories:
            format_school(school_directory, os.path.basename(school_directory))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
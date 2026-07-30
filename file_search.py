import os


def find_file(filename, search_path="D:\\"):

    filename = filename.lower()

    matches = []

    try:
        for root, dirs, files in os.walk(search_path):

            for file in files:

                if filename == file.lower():
                    matches.append(os.path.join(root, file))

        return matches

    except Exception as e:
        return [str(e)]
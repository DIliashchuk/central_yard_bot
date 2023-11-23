import csv


REGISTER_FILE = "register.db.csv"


def write_to_csv(filename, data, mode='a'):
    try:
        with open(f'files/{filename}', mode, newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            csv_writer.writerow(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file '{filename}': {e}")
        return None
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def rewrite_to_csv(filename, data, mode='w'):
    try:
        with open(f'files/{filename}', mode, newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',')
            for row in data:
                csv_writer.writerow(row)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file '{filename}': {e}")
        return None
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")


def read_to_csv(filename):
    try:
        with open(f'files/{filename}', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile, delimiter=',')
            return list(csv_reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found.")
    except csv.Error as e:
        print(f"Error reading CSV file '{filename}': {e}")
        return None
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
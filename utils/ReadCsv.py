import pandas as pd

def read_processes_from_csv(file_path):
    process_list = []
    #we will return a list of dicts not process object list because we want to keep the process class separate from the csv reading logic
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return process_list
    except pd.errors.EmptyDataError:
        print(f"File is empty: {file_path}")
        return process_list

    for i, row in df.iterrows():
        process={
            "process_id": i + 1,
            "burst_time": int(row[0]),  # Assuming burst time is in the first column
            "priority": int(row[1]),  # Assuming priority is in the second column
            "arrival_time": int(row[2])  # Assuming arrival time is in the third column
        }

        process_list.append(process)

    return process_list
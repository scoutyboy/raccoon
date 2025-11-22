import sys
import json

config = { "interesting_table_names": ['user', 'login', 'auth', 'permission', 'network', 'domain', 'config', 'ip'] }

def process_args():
    output_mode = {
        ("total_records", "-nr"),
        ("total_tables", "-nt"),
        ("full_table_list", "-l"),
        ("interesting_objects_search", "-i")
    }

def load_file(file):
    with open(file, 'r') as f:
        return json.load(f)
    
def total_records(results):
    total_record_count = 0
    for res in results:
        total_record_count += res["count"]
    return total_record_count

def total_tables(results):
    return len(results)

def return_all_table_names(results):
    tables = []
    for res in results:
        tables.append(res["name"])
    return tables

def return_interesting_tables(results):
    interesting_tables = []
    for search_term in config["interesting_table_names"]:
        for searched_item in return_all_table_names(results):
            if search_term in searched_item.lower():
                interesting_tables.append(searched_item)
    return interesting_tables

def main():
     results = load_file(sys.argv[1])
     total_record_count = total_records(results)
     print(total_record_count, total_tables(results), return_interesting_tables(results))

main()
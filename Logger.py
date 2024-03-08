import logging

def search_log(log_file, search_keyword):
    try:
        # Configure the logger to read from the log file
        logging.basicConfig(filename=log_file, level=logging.DEBUG)

        # Create a filter to match log records containing the search keyword
        class SearchFilter(logging.Filter):
            def filter(self, record):
                return search_keyword in record.getMessage()

        # Create a logger and add the filter
        logger = logging.getLogger()
        logger.addFilter(SearchFilter())

        # Iterate through all log records and display matching lines
        with open(log_file, 'r') as file:
            for line in file:
                record = logging.makeLogRecord({'msg': line})
                print(record)
                if logger.filter(record):
                    print(line.strip())
    except FileNotFoundError:
        print(f"Error: File not found - {log_file}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

log_file_path = 'example.log'
search_keyword = 'Error'

search_log(log_file_path, search_keyword)

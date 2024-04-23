import pickle
import gzip

# data = {"logins": ["some_login", "sosssn", "sogin"], "password": ["123456", 1213, "sdv"], "info": {"version":
# "1.0", "release": "2024"}} with gzip.open('data1.gz', 'wb') as file: data_serialized = pickle.dumps(data)
# file.write(data_serialized)
#
# with gzip.open('data1.gz', 'rb') as file:
#     read_data = file.read()
#     data_read = pickle.loads(read_data)
#
# print(data_read)


# with open("large_file.txt", 'w') as file:
#     for i in range(100000):
#         file.writelines(f"Line {i} in file")

# with gzip.open('large_file.gz', 'wb') as gzip_file:
#     with open("large_file.txt", "r") as txt_file:
#         data = txt_file.read()
#         serialized_data = pickle.dumps(data)
#         gzip_file.write(serialized_data)
#
# with open('large_file.pickle', 'wb') as pickle_file:
#     with open("large_file.txt", "r") as txt_file:
#         data = txt_file.read()
#         pickle.dump(data, pickle_file)


with gzip.open("large_file.gz", 'rb') as file:
    serialized_data = file.read()
    real_data = pickle.loads(serialized_data)

    lines = real_data.split('\n')
    print(lines[:10], end='\n')

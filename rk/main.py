from faker import Faker
import random

def generate_data(n, filename):
    fake = Faker()
    with open(filename, 'w') as file: 
        for _ in range(n):
            name = fake.name()
            file.write(name+'\n')

def read_file(filename):
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    return data


def full_iteration(names, val):
    if len(names) == 0:
        # print("Warning! Empty dictionary.")
        return None
    for i in range(len(names)):
        if names[i] == val:
            return i+1
    # if result != None:
    #     print("ID = ", result)
    # else:
    #     print("No value")

def bin_search(names, val):
    if len(names) == 0:
        print("Warning! Empty array.")
        return None
    mid, low, high = len(names) // 2, 0, len(names) - 1
    while names[mid] != val and low <= high:
        if val > names[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return None
        # print("No value")
    else:
        return mid
        # print("ID =", tmp[mid][0])





if __name__ == "__main__":
    # for i in range(1000,10000, 1000):
    #     generate_data(i, str(i)+'.csv')
    # data = read_file('1000.csv')
    # result = full_iteration(data, 'Tina Henson')
    
    names = ['Robert Rodriguez', 'James Huang', 'Judy Medina',
             'Nicholas Lawrence', 'Joseph Ramirez', 'Patrick Williams',
             'Alexis White', 'Bridget Farley', 'Timothy Erickson'] 
    for i in range(len(names)):
        data = read_file(str((i+1)*1000) + '.csv')
        data.sort()
        print("Value: ", names[i], "|| Result: ", bin_search(data, names[i]))
    
    
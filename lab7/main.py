from faker import Faker
import random
import csv

def generate_data(n, filename):
    fake = Faker()
    with open(filename, 'w') as csvfile:
        fieldnames = ['id', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
        writer.writeheader()
        for i in range(n):
            id = random.randint(500000, 900000)
            email = fake.email()
            writer.writerow({'id': id, 'email': email})

def read_csv(filename):
    emails = dict()
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            emails[row['id']] = row['email']
    return emails

def sort(emails, reverse):
    tmp = dict()
    list_d = list(emails.items())
    if reverse == False:
        list_d.sort(key = lambda i: i[1], reverse = False)
    else:
        list_d.sort(key = lambda i: i[1], reverse = True)
    for i in list_d:
        tmp[i[0]] = i[1]
    return tmp

def full_iteration(emails, val):
    if len(emails) == 0:
        # print("Warning! Empty dictionary.")
        return None
    result = None
    for key, value in emails.items():
        if value == val:
            result = key
    # if result != None:
    #     print("ID = ", result)
    # else:
    #     print("No value")
    return result

def bin_search(emails, val):
    if len(emails) == 0:
        print("Warning! Empty dictionary.")
        return None
    emails = sort(emails, False)
    mid, low, high = len(emails) // 2, 0, len(emails) - 1
    tmp = tuple(emails.items())
    while tmp[mid][1] != val and low <= high:
        if val > tmp[mid][1]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
    if low > high:
        return None
        # print("No value")
    else:
        return tmp[mid][0]
        # print("ID =", tmp[mid][0])

def check(a, value):
    for i in a:
        for j in i:
            if value in j:
                return True
    return False

def make_dict(arr):
    tmp = []
    for i in arr:
        if len(i) > 1:
            b = {}
            for j in i:
                b[j[0]] = j[1]
            tmp.append(b)
        else:
            b = {}
            b[i[0][0]] = i[0][1]
            tmp.append(b)
    return tmp
   
def analyse(emails):
    arr = []
    items = emails.items()
    for i in items:
        flag = False
        tmp = []
        for j in items:
            if i[1][0] == j[1][0] and i[1] != j[1]:
                flag = True
                if not check(arr, i[1]):
                    tmp.append(j)
                    tmp.append(i)
                    
        if len(tmp) != 0:
            arr.append(tmp)
        if flag == False:
            a = []
            a.append(i)
            arr.append(a)
    arr = make_dict(arr)
    return arr



def combined(emails, val):
    if len(emails) == 0:
        print("Warning! Empty dictionary.")
        return None
    arr = analyse(emails)
    arr = sorted(arr, key = len, reverse = True)
    copy = arr
    for i in range(len(copy)):
        tmp = tuple(copy[i].values())
        if tmp[0][0] == val[0]:
            return bin_search(arr[i], val)
            



if __name__ == "__main__":
    # generate_data()
    # emails = read_csv('emails.csv')
    # emails = {}
    # full_iteration(emails, 'george20@hotmail.com')
    # bin_search(emails, 'jessica99@yahoo.com')
    
    # combined(emails, 'george20@hotmail.com')
    names = ['robertpugh@sanchez.com', 'neaton@hotmail.com', 'veronicafisher@gmail.com',
             'lpatterson@yahoo.com', 'qdavis@davis.com', 'seanwood@black.com',
             'gthomas@hotmail.com', 'cody31@harris.com', 'bauermark@hotmail.com', 'cbailey@hotmail.com']
    for i in range(len(names)):
        emails = read_csv(str((i+1)*1000) + '.csv')
        print("KEy: ", names[i], "Result: ", bin_search(emails, names[i]))
    
    
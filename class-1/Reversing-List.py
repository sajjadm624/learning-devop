# Author
#     Sazzad Hossain
#     Software Engineer, Leads Corporation LTD.

def main():
    n = [2,3,4,5,6,7] # given stirng.
    print('Given String:', n)
    print('Reverse of the string:', reverse_list(n))

def reverse_list(n):
    
    length = len(n) # taking the length.
    
    for i in range(int(length/2)):
        n[i], n[length-1-i] = n[length-1-i], n[i] # swapping the items with from very leftmost and very rightmost.
    return n
  
main()

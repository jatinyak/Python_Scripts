# N = input()
# N_int = int(N)
# M = input()
# M_int = int(M)
# Total_no_bills = N_int / M_int
# print(Total_no_bills)

# N = "126.5"
# M = float(N)
# print(M)


# N = int(input())
# if ( N % 2 ) == 0:
#     print(0)
# else:
#     print(1)


# print((3 + 4) // 2 + 6)

# print(True == 1)

# print("1" != 1)


# A = int(input())
# if A >= 2100:
#     print('GRAND MASTER')
# elif A >= 1900 and A < 2100:
#     print('CANDIDATE MASTER')
# elif A >= 1600 and A < 1900:
#     print('EXPERT')
# elif A >= 1400 and A < 1600:
#     print('PUPIL')
# elif A < 1400:
#     print('NEWBIE')
# else:
#     print('Invalid')


# x = 2
# if x==2:
#     x = 3
#     x = 4
# else:
#     x = 5
# print(x)
# x=3
# if x > 2:
#     x = x*2
# if x > 4:
#     x = 0
# print(x)

# print( -9 % -2 )

# n=8
# while n>=0:
#    n -= 2
#    if n%2==0:
#        continue
#    print(n, end=" ")
# else:
#    print("Exec", end=" ")

# i=2
# if i==2:
#     i+=1
# for j in range(i):
#     pass
#     break
#     i+=1
# print(i)


# N = int(input())
# M = int(input())
# start = 0
# while start < M:
#     start += 1
#     transaction = input()
#     Type = int(transaction[0:1])
#     Amount = int(transaction[2:])
#     if Type == 1:
#         N += Amount
#     elif Type == 2:
#         if N > Amount:
#             N -= Amount
#         else:
#             print("Insufficient Funds")
#             continue
#     else:
#         continue
#     print(N)


# N = int(input())
# for i in range(2, N):
#     if N % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")



# N = int(input())
# while N > 0:
#     digit = N % 10
#     print(digit)
#     N = N // 10

# N = int(input())
# sum_digits = 0
# while N > 0:
#     digit = N % 10
#     sum_digits += digit 
#     N = N // 10
# print(sum_digits)

# N = int(input())
# reverse_digits = 0
# while N > 0:
#     digit = N % 10
#     reverse_digits = reverse_digits * 10 + digit
#     N = N // 10
# print(reverse_digits)


# N = int(input())
# reverse_digit = 0
# while N!=0:
#     digit=N%(-10)
#     reverse_digit = reverse_digit * 10 + digit
#     N=-(N//-10)
# print(reverse_digit)
# for i in range(1,6):
#     print(' '*(5-i) + '*'*i)


# A = int(input())
# for i in range(2,A):
#     if A % i == 0:
#         print('NO')
#         break
# else:
#     print('YES')


# i = 0
# j = 0
# while i <= 2:
#    if j%2:
#        j += 1
#    print(i, ":", j, end=" ")
#    i+=1
#    j+=1


# N = input()
# L = N.split(' ')
# first = 0
# second = 0
# for i in range(len(L)): 
#     L[i] = int(L[i])
# first = int(L[0])
# second = int(L[1])
# highest_comman_divisor = 0
# if first < second:
#     smaller = first
# else:
#     smaller = second
# for j in range(smaller,0,-1):
#     if (first % j == 0) and (second % j == 0):
#         highest_comman_divisor = j
#         break
# print(highest_comman_divisor)


# def func1(name,age):
#     print("Name:",name)
#     print("Age:",age)
#     return

# func1(23,"mohit")


# A = list(map(int(input().split())))
# A = A[1:]
# print(A.max(),A.min())

# class Solution:
#     # @param A : list of list of integers
#     # @return a list of integers
#     def solve(self, A):
#         def max_in_row(row):
#             if not row:  # Handle empty row
#                 return 0
#             largest_number = row[0]  # Initialize with first element instead of 0
#             for i in row:
#                 if i > largest_number:
#                     largest_number = i
#             return largest_number
        
#         output_list = []
#         for i in A:
#             output_list.append(max_in_row(i))
        
#         return output_list  # RETURN the list, don't print it

# # Test with the platform's input
# A = [[1, 2], [1, 3]]
# solution = Solution()
# result = solution.solve(A)
# print(result)  # This should print [2, 3]


# def main():
#     # YOUR CODE GOES HERE
#     # Please take input and print output to standard input/output (stdin/stdout)
#     # E.g. 'input()/raw_input()' for input & 'print' for output
#     order_of_matrix = list(map(int,input().split()))

#     def input_matrix_row():
#         return list(map(int,input().split()))

#     def print_matrix_row(row):
#         for i in row:
#             print(i, end=' ')

#     matrix = []
#     for _ in range(order_of_matrix[0]):
#         matrix.append(input_matrix_row())

#     row_index = 0

#     for row in matrix:
#         print(str(row_index) + 'th row -> ', end='')
#         print_matrix_row(row)
#         print()
#         row_index += 1

#     return 0

# if __name__ == '__main__':
#     main()

# # Code to remove an element from a list at a given index

# # Method 1: Using pop() method
# A = [1, 2, 3, 5, 6, 7, 8]
# index_to_remove = 3  # Remove element at index 3 (which is 5)
# print("Original list:", A)

# # Remove element using pop()
# removed_element = A.pop(index_to_remove)
# print(f"Removed element: {removed_element}")
# print("List after removal:", A)

# print("-" * 40)

# # Method 2: Using del statement
# B = [10, 20, 30, 40, 50, 60]
# index_to_remove = 2  # Remove element at index 2 (which is 30)
# print("Original list:", B)

# del B[index_to_remove]
# print("List after removal:", B)

# print("-" * 40)

# # Method 3: Using list slicing
# C = ['a', 'b', 'c', 'd', 'e']
# index_to_remove = 1  # Remove element at index 1 (which is 'b')
# print("Original list:", C)

# C = C[:index_to_remove] + C[index_to_remove + 1:]
# print("List after removal:", C)

# print("-" * 40)

# # Method 4: Safe removal with index validation
# def remove_at_index(lst, index):
#     """Safely remove element at given index"""
#     if 0 <= index < len(lst):
#         return lst.pop(index)
#     else:
#         print(f"Index {index} is out of range for list of length {len(lst)}")
#         return None

# # Test the safe removal function
# D = [100, 200, 300, 400, 500]
# print("Original list:", D)

# # Valid index
# removed = remove_at_index(D, 2)
# print(f"Removed: {removed}, List: {D}")

# # Invalid index
# removed = remove_at_index(D, 10)
# print(f"List after invalid removal attempt: {D}")

# print("-" * 40)

# # Interactive example
# E = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print("Original list:", E)
# print("Enter index to remove (0 to", len(E)-1, "):")

# # Uncomment the lines below for interactive input
# # try:
# #     user_index = int(input())
# #     if 0 <= user_index < len(E):
# #         removed = E.pop(user_index)
# #         print(f"Removed element {removed} at index {user_index}")
# #         print("Updated list:", E)
# #     else:
# #         print("Invalid index!")
# # except ValueError:
# #     print("Please enter a valid number!")


# A = [[1, 2, 3] , [4, 5 , 6] , [7, 8, 9] ]
# B = [[10,11,12],[13,14,15],[16,17,18]]
# X = 0
# for i in range(X,len(A)-1):
#     A[i] = A[i+1]
# A.pop()
# print(A)

# A = [[1, 2, 3] , [4, 5 , 6] , [7, 8, 9] ]
# B = [[10,11,12],[13,14,15],[16,17,18]]
# result = [ [A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A)) ]
# print(result)

# # Initialize global variables
# inp = []
# ii = 0

# def main():
#     # DO NOT CHANGE THE CODE BELOW.
#     global ii
#     n = inp[ii: ii + 1][0]
#     ii += 1
#     mat = [[0 for i in range(n)] for j in range(n)]
#     for i in range(n):
#         for j in range(n):
#             mat[i][j] = inp[ii: ii + 1][0]
#             ii += 1
#     # DO NOT CHANGE THE CODE ABOVE
    
#     # YOUR CODE GOES BELOW HERE.
#     # USE THE GIVEN MATRIX mat FOR ALL THE OPERATIONS.

#     def right_left(row):
#         for i in range(len(row)-1, -1, -1):  # Fixed: should go to -1, not 0
#             print(row[i], end=' ')

#     def left_right(row):
#         for i in range(len(row)):  # Fixed: removed +1 which caused index error
#             print(row[i], end=' ')

#     for i in range(len(mat)):
#         if i % 2 == 0:
#             left_right(mat[i])
#         else:
#             right_left(mat[i])
#         print()  # Add newline after each row
    
#     return 0

# if __name__ == '__main__':
#     # Sample test data - replace this with actual input mechanism
#     # inp should contain: [n, mat[0][0], mat[0][1], ..., mat[n-1][n-1]]
#     inp = [3, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 3x3 matrix with values 1-9
#     main()


# class Solution:
#     # @param A : list of list of integers
#     # @return a list of list of integers
#     def solve(self, A):
#         # Handle empty matrix
#         if not A:
#             return A

#         rows = len(A)
#         cols = len(A[0])

#         # Ensure matrix is rectangular (no ragged rows)
#         for row in A:
#             if len(row) != cols:
#                 raise ValueError("All rows must have the same number of columns")

#         # If not square, return a new transposed matrix instead of attempting in-place swap
#         if rows != cols:
#             return [[A[r][c] for r in range(rows)] for c in range(cols)]

#         # In-place transpose for square matrix
#         for i in range(rows):
#             for j in range(i + 1, cols):
#                 A[i][j], A[j][i] = A[j][i], A[i][j]

#         return A
    

import os

def combine_files_for_notebooklm(source_folder, max_size_mb=5.0):
    """
    Combines text-based files from a nested directory into chunked .txt files
    and saves them in the current working directory.
    """
    if not os.path.exists(source_folder):
        print(f"Error: The folder '{source_folder}' does not exist.")
        return

    # Use the current working directory (pwd) for output
    output_folder = os.getcwd()
    
    # Convert Megabytes to Bytes
    max_size_bytes = int(max_size_mb * 1024 * 1024)
    
    # Extensions tailored to skip images/binaries and target code/text files.
    ALLOWED_EXTENSIONS = {
        '.txt', '.md', '.py', '.js', '.json', '.xml', '.html', 
        '.css', '.abap', '.properties', '.csv', '.yaml', '.yml','.doc'
    }

    file_part = 1
    current_size = 0
    
    current_out_filepath = os.path.join(output_folder, f"PE_Data_elements_with_Docu_{file_part}.txt")
    out_file = open(current_out_filepath, 'w', encoding='utf-8')

    # Walk through the provided directory
    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            ext = os.path.splitext(filename)[1].lower()
            
            if ext not in ALLOWED_EXTENSIONS:
                continue

            filepath = os.path.join(root, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8', errors='replace') as in_file:
                    content = in_file.read()

                header = f"\n\n{'='*50}\nFILE PATH: {filepath}\n{'='*50}\n\n"
                text_to_write = header + content
                
                text_size_bytes = len(text_to_write.encode('utf-8'))

                # Chunk to a new file if size exceeds the limit
                if current_size + text_size_bytes > max_size_bytes and current_size > 0:
                    out_file.close()
                    file_part += 1
                    current_out_filepath = os.path.join(output_folder, f"PE_Data_elements_with_Docu_{file_part}.txt")
                    out_file = open(current_out_filepath, 'w', encoding='utf-8')
                    current_size = 0

                out_file.write(text_to_write)
                current_size += text_size_bytes

            except Exception as e:
                print(f"Warning: Could not read {filepath}. Reason: {e}")

    out_file.close()
    
    # Cleanup: If the last file created is empty, delete it
    if current_size == 0 and os.path.exists(current_out_filepath):
        os.remove(current_out_filepath)
        file_part -= 1 if file_part > 1 else 0

    if file_part > 0 and current_size > 0:
        print(f"\nProcess complete! Generated {file_part} file(s) in your current directory: {output_folder}")
    else:
        print("\nNo valid text/code files were found to combine.")

if __name__ == "__main__":
    # 1. Ask the user for the folder path
    folder_input = input("Enter the full path of the folder to process: ").strip()
    
    # 2. Handle quotes (useful if dragging and dropping a folder into the terminal)
    if (folder_input.startswith('"') and folder_input.endswith('"')) or \
       (folder_input.startswith("'") and folder_input.endswith("'")):
        folder_input = folder_input[1:-1]

    print(f"\nScanning '{folder_input}'...")
    
    # 3. Run the combination process
    combine_files_for_notebooklm(folder_input)

# from pathlib import Path

# # Configure these paths
# INPUT_DIR = Path("/Users/jatin.s/Desktop/SRTP/EPC258_22_Payee_Payee_RTP_SP_SRTP_IG_V4_XSD")
# OUTPUT_DIR = Path("/Users/jatin.s/Desktop/SRTP/EPC258_22_Payee_Payee_RTP_SP_SRTP_IG_V4_XSD")
# OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# def is_likely_text(data: bytes) -> bool:
#     # Heuristic: if null byte exists, likely binary
#     if b"\x00" in data:
#         return False
#     # Try UTF-8 decode
#     try:
#         data.decode("utf-8")
#         return True
#     except UnicodeDecodeError:
#         return False

# for src in INPUT_DIR.rglob("*"):
#     if not src.is_file():
#         continue

#     rel = src.relative_to(INPUT_DIR)
#     out_file = (OUTPUT_DIR / rel).with_suffix(src.suffix + ".txt")
#     out_file.parent.mkdir(parents=True, exist_ok=True)

#     data = src.read_bytes()

#     if is_likely_text(data):
#         # Keep original text content
#         text = data.decode("utf-8", errors="replace")
#         out_file.write_text(text, encoding="utf-8")
#     else:
#         # For binary files, write a readable placeholder + hex dump preview
#         preview = data[:2048].hex()
#         content = (
#             f"Original file: {src}\n"
#             f"Type: binary\n"
#             f"Size: {len(data)} bytes\n"
#             f"Hex preview (first 2048 bytes):\n{preview}\n"
#         )
#         out_file.write_text(content, encoding="utf-8")

# print("Done: converted files to .txt in", OUTPUT_DIR)
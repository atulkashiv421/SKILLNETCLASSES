# def tri_recusion(k):
#     if(k>0):
#         result=k+tri_recusion(k+1)
#         print(result)
#     else:
#         result=0
#         return result
# print("Recusion example results")
# tri_recusion(6)

# def is_palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     return is_palindrome(s[1:-1])
# word=input("Enter a word: ")
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word}is not a palindrome")

import random
def guess_number(secret,attempts=1):
    guess=int(input(f"Attempt {attempts}: guess the number (between 1 to 10):"))
    if guess < secret:
        print("too low try again.")
        return guess_number(secret,attempts +1)
    elif guess >secret:
        print("too high try again")
        return guess_number(secret,attempts + 1)
    elif guess == secret:
     print(f"congs ! you have guesse the number {secret} in {attempts} attempts.")
     return attempts 

    

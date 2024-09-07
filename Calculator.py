#!/usr/bin/env python
# coding: utf-8

# In[22]:


def operation():
    while True:
        try:
            a = float(input('Enter the first number'))
            print(f"a= {a}")
            b = float(input('Enter the second number'))
            print(f"b = {b}")
            print("""Arithmetic Operations
              1. Addition 
              2. Subtraction
              3. Multiplication
              4. Division
              """)

            while True:
                try:
                    
                
                    c = int(input('Choose the operation number which you want to perform'))
                    if c == 1:
                        print(a + b)
                        break
                    elif c == 2:
                        print(a - b)
                        break
                    elif c == 3:
                        print(a * b)
                        break
                    elif c == 4:
                        if b == 0:
                            print('Denominator cannot be zero. Please enter number other than zero for denominator')
                            break
                        else:
                            print(a/b)
                            break
                    else:
                        print('choose correct operation number')

                
                except:
                    print('Please enter number only')
                        
            
            while True:
                
                d = input('Do you want to perform another calculation (yes/no)? ').strip().lower()
                if d == 'yes':
                    break
                elif d == 'no':
                    print('Goodbye')
                    return
            
                else:
                    print('Please enter yes or no. Do you want to perform another operation?')
                

        except:
            print('Please enter number only')

operation()


# In[ ]:





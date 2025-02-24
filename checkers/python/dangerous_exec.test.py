def dummy_func():
    # Inputs from user can be malicious
    user_inp = input()
    # <expect-error>
    exec(user_inp)

# Hard coded strings are fine
exec("knows what to do")
    
# However, modifiable variables are not fine
evil_string = "Do evil"
# <expect-error>
exec(evil_string)
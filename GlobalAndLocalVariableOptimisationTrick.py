global_var =10

def func():
    ans  = 0
    for i in range(1000):
        ans += global_var * 1
        return ans

print(func())

# In this function there is a big optimisation problem whenever this function is invoked it will look for
# global_var in its local scope but this variable is in the global scope so Python Virtual machine has
# to look into the gobal scope to get the variables values

# so what we can do is we can assigned this global variable to local variable 
# inside the function


def func1():
    local_var = global_var
    ans=0
    for i in range(1000):
        ans += local_var * 1
        return ans

print(func1())

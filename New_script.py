# Test script

fake_array = [1,2,3,4,5]

def main() -> None:
    for i,f, in enumerate(fake_array):
        print('Iteration: ' + str(i) + ', Value: ' + str(f))
        

main()

# New function created in branch
def new_function():
    print("New function")
new_function()
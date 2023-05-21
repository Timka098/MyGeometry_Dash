import os

# повний шлях 
def abspath(path):
    return os.path.join(os.path.abspath(__file__ + '/..'), path)
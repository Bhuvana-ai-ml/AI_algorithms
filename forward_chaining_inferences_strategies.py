
parents = {
    ('john', 'mary'),
    ('john', 'david'),
    ('susan', 'mary'),
    ('susan', 'david'),
    ('mary', 'linda'),
    ('mary', 'steve')
}

male = {'john', 'david', 'steve'}
female = {'susan', 'mary', 'linda'}

def is_parent(x, y):
    return (x, y) in parents

def is_male(x):
    return x in male

def is_female(x):
    return x in female

def father(x, y):
    return is_parent(x, y) and is_male(x)

def mother(x, y):
    return is_parent(x, y) and is_female(x)

def grandparent(x, y):
    return any(is_parent(x, z) and is_parent(z, y) for z in all_people())

def sibling(x, y):
    if x == y:
        return False
    return any(is_parent(z, x) and is_parent(z, y) for z in all_people())


def all_people():
    return set(x for x, _ in parents) | set(y for _, y in parents)


print("father(john, mary):", father('john', 'mary'))           
print("mother(susan, david):", mother('susan', 'david'))     
print("grandparent(john, linda):", grandparent('john', 'linda'))  
print("sibling(mary, david):", sibling('mary', 'david'))   

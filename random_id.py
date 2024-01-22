import random

def random_id_generator(n):
    alphabates =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    product_id = ""
    while len(product_id) != n:
        step = random.randint(0,3)
        if step == 1:
            product_id += str(alphabates[random.randint(1,25)])
        elif step == 2:
            product_id += str(alphabates[random.randint(0,5)].lower())
        elif step == 3:
            product_id += str(random.randint(0,9))
    return product_id


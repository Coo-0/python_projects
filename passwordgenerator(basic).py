import secrets
import string

n=int(input())
def generate(length=n,upper=True,lower=True,digits=True,symbols=True):
    all=''

    if lower:
        all+=string.ascii_lowercase
    if upper:
        all+=string.ascii_uppercase
    if digits:
        all+=string.digits
    if symbols:
        all+=string.punctuation
    return ''.join([secrets.choice(all) for i in range(length)])

if __name__ =="__main__":
    print(generate())
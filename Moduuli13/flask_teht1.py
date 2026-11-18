from flask import Flask, request

app = Flask(__name__)


def isprime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

num = 31

@app.route(f'/prime_number/{num}')

def check_prime():
    resp = isprime(num)
    return str(f"Number : {num} isPrime:{resp}")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
    
    

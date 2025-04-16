from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<luku>')
def check_prime(luku):
    try:
        numero = int(luku)
        tulos = is_prime(numero)

        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "Number": numero,
            "isPrime": tulos
        }

    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen syöte, ei kelpaa kokonaisluvuksi"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

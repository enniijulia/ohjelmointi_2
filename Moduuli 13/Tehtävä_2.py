import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    print("Yhteys tietokantaan...")
    return mysql.connector.connect(
        host='localhost',
        user='python',
        password='py123',
        database='flight_game'
    )

@app.route('/kenttä/<icao>', methods=['GET'])
def hae_kentta(icao):
    print(f"Haetaan kenttä: {icao}")
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT ident AS ICAO, Name, Municipality FROM airport WHERE ident = %s"
        cursor.execute(query, (icao,))
        kentta = cursor.fetchone()

        cursor.close()
        conn.close()

        if kentta:
            print(f"Löytyi kenttä: {kentta}")
            return jsonify({
                "ICAO": kentta['ICAO'],
                "Name": kentta['Name'],
                "Municipality": kentta['Municipality']
            })
        else:
            print("Kenttää ei löytynyt.")
            return jsonify({"message": "Lentokenttää ei löytynyt."}), 404

    except mysql.connector.Error as err:
        print(f"Tietokantavirhe: {err}")
        return jsonify({"message": f"Tietokantavirhe: {err}"}), 500
    except Exception as e:
        print(f"Yleinen virhe: {e}")
        return jsonify({"message": f"Yleinen virhe: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)


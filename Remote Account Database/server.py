from flask import Flask, request

app = Flask(__name__)

ipaddress = 'localhost' #IP Remote Account Database is hosted on
port = 25565 #Port Remote Account Database is hosted on
#Web URL: http://localhost:25565/check_database


# define the endpoint for checking email and password
@app.route('/check_database', methods=['POST'])
def check_login():
    email = request.form['email']
    password = request.form['password']

    #print(f'Email:{email} Password:{password}')

    # read the CSV file and check for email and password
    with open('accountdatabase.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            if email == line[0] and password == line[1]:
                return line[2]
    
    return "login failed"

if __name__ == '__main__':
    app.run(ipaddress,port)

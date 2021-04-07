from flask import Flask, request

apps = Flask(__name__)

@apps.route('/')
def index():
    # mengambil header dari objek request 
    headers = request.headers
    respone = ['%s = %s' % (key, value) for key, value in sorted(headers.items())]
    # respone ='</br>' .join(respone)
    respone =  '<br>' .join(respone)
    return respone
    # return request.headers.get('User-Agent')

if __name__ == "__main__":
    apps.run(debug=True)
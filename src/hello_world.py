from flask import Flask
app = Flask( __name__ )

@app.route( "/")
def hello():
    return "Hello World!"

if __name__== "__main__" :
    
    context = ('/etc/ssl_certs/cert.pem', '/etc/ssl_certs/key.pem')#certificate and key files
    app.run( host='0.0.0.0', port=8087,  ssl_context = context )
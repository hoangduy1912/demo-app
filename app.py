from flask import Flask
app = Flask('hello-cloudbuild')

@app.route('/')
def hello():
  return "Application Version 1\n"

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 8080)
from flask import Flask
from threading import Thread

app = Flask('')

@app.route("/")
def main():
  return "Hello there you use pandagamerfx bot commands"

def run():
  app.run(host="0.0.0.0",port = 8080)

def keep_alive():
  server= Thread(target=run)
  server.start()
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/")
def home():

@app.route("/product/<int:item_id>")
def get_product(item_id):
  return jsonify

from flask import Flask, render_template, request, jsonify
from database_helper import DatabaseHelper
from llm import LLM

app = Flask(__name__)
app._static_folder = './static'
db_helper = DatabaseHelper('static/json/database.json')
llm = LLM()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/order")
def order():
    return render_template("order.html")


@app.route("/sales")
def sales():
    return render_template("sales.html")


@app.route("/query")
def query():
    rest_name = request.args.get("rn")
    food_type = request.args.get("ft")
    rand_seed = request.args.get("rs")
    rand_seed = float(rand_seed) if rand_seed else None
    query_result = db_helper.rand_pick(food_type, rand_seed)
    return jsonify(query_result)


@app.route("/call_llm_hint", methods=["POST"])
def call_llm_hint():
    try:
        if request.method == "POST":
            question = request.form['question']
            # logging.debug(f"Received question: {question}")
            # 模擬處理，這裡可以根據實際需要調用 llm.invoke 進行處理
            result = llm.invoke(question)
            return jsonify({'answer': result.content})
    except Exception as e:
        # logging.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run()

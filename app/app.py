from flask import Flask, render_template, request
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import config
from extensions import db, migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{config.DB_USERNAME}:{config.DB_PASSWORD}@{config.DB_HOST}/{config.DB_DATABASE}"

db.init_app(app)
migrate.init_app(app, db)


@app.route('/', methods=["GET"])
def index():
    # 使用 Plotly 創建一個簡單的圖表
    fig = make_subplots(rows=1, cols=1)

    trace = go.Scatter(x=[1, 2, 3, 4, 5], y=[10, 11, 12,
                       13, 14], mode='lines', name='Line Plot')
    fig.add_trace(trace)

    fig.update_layout(
        title='Plotly Chart in Flask',
        xaxis=dict(title='X軸標籤'),
        yaxis=dict(title='Y軸標籤')
    )

    # 將圖表嵌入到 HTML 響應中
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)


@app.route('/', methods=["POST"])
def create():
    data = request.get_json()


if __name__ == '__main__':
    app.run(debug=True)

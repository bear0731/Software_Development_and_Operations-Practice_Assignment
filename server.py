from flask import Flask, send_from_directory, jsonify
import os

app = Flask(__name__)

# 設定存放照片的資料夾
PHOTO_DIRECTORY = "photos"
port = 33000

@app.route('/photos', methods=['GET'])
def list_photos():
    try:
        files = os.listdir(PHOTO_DIRECTORY)
        image_files = [f for f in files if f.endswith(('.jpg', '.jpeg', '.png'))]
        return jsonify(image_files)
    except Exception as e:
        return str(e), 500

@app.route('/download/total_sales_over_time')
def download_sales_over_time():
    try:
        return send_from_directory(PHOTO_DIRECTORY, "total_sales_over_time.png", as_attachment=True)
    except FileNotFoundError:
        return "照片未找到", 404

@app.route('/download/total_sales_by_region')
def download_sales_by_region():
    try:
        return send_from_directory(PHOTO_DIRECTORY, "total_sales_by_region.png", as_attachment=True)
    except FileNotFoundError:
        return "照片未找到", 404

@app.route('/download/total_sales_by_category')
def download_sales_by_category():
    try:
        return send_from_directory(PHOTO_DIRECTORY, "total_sales_by_category.png", as_attachment=True)
    except FileNotFoundError:
        return "照片未找到", 404

@app.route('/download/top_10_best_performing_products')
def download_top_products():
    try:
        return send_from_directory(PHOTO_DIRECTORY, "top_10_best_performing_products.png", as_attachment=True)
    except FileNotFoundError:
        return "照片未找到", 404

if __name__ == '__main__':
    app.run(debug=True, port=port)
    print(f"網址: http://localhost:{port}/photos")

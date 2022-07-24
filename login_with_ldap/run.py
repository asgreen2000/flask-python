import sys
from app import create_app

if __name__ == '__main__':
    product_env = "development" if len(sys.argv) < 2 else sys.argv[1]
    app = create_app(product_env)
    app.run(debug=True)
    # app.run(host='
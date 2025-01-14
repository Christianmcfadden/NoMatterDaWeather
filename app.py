from NMDW import app
from flask_wtf.csrf import CSRFProtect

if __name__ == '__main__':
    app.run(debug=False)

csrf = CSRFProtect(app)
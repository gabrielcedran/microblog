from app import app

@app.route('/test')
def test():
    return 'testing stuff'
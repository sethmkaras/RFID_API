#!flask/bin/python
from app import app
import os
port = int(os.environ.get('PORT', 9000))
#app.run(host='192.168.1.159', port=5000)
app.run(debug=True, port=port)

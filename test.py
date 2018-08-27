from flask import Flask
from flask import request


import DETECTION

app=Flask(__name__)


# @app.route('/blah', methods=['GET'])
# def index():
#     BUCKET_NAME = 'sinchan.face'  # replace with your bucket name
#     KEY = 'logo.png'  # replace with your object key
#
#     s3 = boto3.resource('s3')
#     s3.Bucket(BUCKET_NAME).download_file(KEY, './input/my_local_image.jpg')
#     return "done"
@app.route('/check',methods=['POST'])
def index1():
    DETECTION.main()
    return "True"

@app.route('/getObstacles',methods=['POST'])
def index():
    return "True"

if (__name__)=="__main__":
    app.run(debug=True)

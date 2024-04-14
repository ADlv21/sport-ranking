import boto3
import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def root():
    return {"status" : 'successfull'}, 200

@app.route('/queue', methods=['POST'])
def add_to_queue():
    
    body = request.data
    message_data = json.loads(body)
    
    sqs = boto3.client(
        'sqs',
        aws_access_key_id='ASIATUYJP7SUGPFIGMXY',
        aws_secret_access_key='AGupVk+zfVd4fQ3B28PxIithIoJzSrG7UqS07g/H',
        aws_session_token='IQoJb3JpZ2luX2VjEFAaCXVzLWVhc3QtMSJIMEYCIQDXtjM29pvobi4fOB2uu2j4Anoo6gTiWIMRqS65W3V1WgIhAMIeu4pdZBc9JhzRP/12l1SnVc0+KcjzlikF7VwN18NcKvsDCHkQAxoMMjUwNzM4NjM3OTkyIgx3YETzj3tqdauk9SAq2AM2AEVekqk+JiRic6e8mA9shdii3gbhBGOO0kyi6TDR/M4TJioknhvO9bvgByADKBPkQI9g0WXiuZuVfp2sqnMNtyv4m8hE4DrvKQrCI4wJ5b2JZ6xnrdlTUFOpKd10ZU3B29wSs/w/8m8q8raM5RC5MQsGQRVJgFQnqgEZEKR8mqYOxsV3/f9j9AN+q2Mp2VZSyiKKjz3f+D+Z5+/Ql9drA1OKOTZKgn7HNfisjnbnuq6JziFVY7xPQdwUtuyeWcKR3IoRhUE9f6tJAtKdLsmAvNzIcFrrw5pIE0uFNTV3de0qIx7/txGlzSB+JcX+f1MQbth2s1ce/QHAUc9XWqGvEIQ1sv9Q5bX/BQq3ZMjGTCMi7lJ1kDVbmeD7S82saZ8PEej1bDDGa/KOHw8KiVWIBNxN7m/Z9RPOjOYkvwLvebDFFnm55uSbhg4Mdbz/TkEUSTS9BRyw+9/Dq2/8gH7JMJ/OBjUfoQecO28/723Q6m6kOMYE2zNMfOtugcwsFWGPMSUM47S/3iwQQvAJL2GCg8KllFx/YqysOhXqea3A0Fl4PljB815gp8lsgrxUpHwsmAmibpOapt0RmRpcKVCmsdDYYJbhdQfkv4RjNCmhNvySYm+XU6LQMO33tbAGOqUB7PAKBu0pZ0zFilvfk8RgrJi/3OBiTnUG7Ej2q3WRjD4oQyxMox4sJhW9kDRqTV6sSqn8pL8b4DGbXiAvnrE5/sBbpHqLON0oH4aI25SDbDk+CIR4TLeqsggwAFmdSw7H+9KgmlLb0rwVD6QBTnBOIr+KZa/rp90XomJdTkiT2HU+rJkZmkDyxvYICuj83Z3f3x4hgAhUHIonKj8xWcd/1jr6EiEC',
        region_name='eu-west-1'
    )
    
    queue_url = 'https://sqs.eu-west-1.amazonaws.com/250738637992/medicine-queue'
    response = sqs.send_message(QueueUrl=queue_url,DelaySeconds=10, MessageBody=json.dumps(message_data))
    
    return {'messageid' : str(response['MessageId'])}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
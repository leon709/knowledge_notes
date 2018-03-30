import json
from flask import request, Flask
from flask.ext.restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class FortuneBase(object):
    
    def __init__(self):
        # load the prepared fortune message data
        self.fortune_base = json.load(file('lm.json'))
        print(self.fortune_base)
        print("fortune base built!")
        self.msg_id_linked_list = self.build_linked_list(self.fortune_base.keys())
    
    def build_linked_list(self, msg_id_list):
        '''build a linked list with the msg_id_list
        '''
        #linked_list = []
        #return linked_list
        return msg_id_list
    
    def del_fortune(self, fortune_id):
        print("del fortune: {}".format(fortune_id))

fb = FortuneBase()

class Fortune(Resource):
    def get(self):
        return {'msg': 'one random fortune message'}, 200

    def post(self):
        print('post')
        data = request.form['data']
        return {'msg_id': 'msgid-xxxx'}, 200
    
    def delete(self, fortune_id):
        fb.del_fortune(fortune_id)
        return '', 204


api.add_resource(Fortune,
                '/fortune')

# 
# @app.route('/fortune', methods=['GET'])
# def fortune():
#     print("handler get request...")
#     return 'msg: xxx'
# 
# @app.route('/fortunes', methods=['POST'])
# def fortunes():
#     '''Add new fortune message to our message database
#     post data: {'msg': 'the fortune message'}
#     Return:
#         The message ID if success
#     '''
#     print("handler POST request...")
#     msg = request.form.get('msg')
# 
#     return 'msg: xxx'
# 
# 
# @app.route('/fortunes/<fortune_id>', methods=['DELETE'])
# def del_fortunes(fortune_id):
#     print("fortunes del: {}".format(fortune_id))
#     msg = request.form.get('msg')
# 
#     return 'msg: xxx'


if __name__ == '__main__':

    app.run(debug=True)

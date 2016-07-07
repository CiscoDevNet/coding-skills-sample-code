import json
import requests

accessToken = "" #set your access token here


def setHeaders():     
    global spark_header
    accessToken_hdr = 'Bearer ' + accessToken
    spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}     


def createRoom(room_name):
    roomInfo = '{"title" :"' + room_name + '"}'
    uri = 'https://api.ciscospark.com/v1/rooms'
    resp = requests.post(uri, data=roomInfo, headers=spark_header)
    print("SparkAPI: ",resp)
    print(resp.json())
    print("Newly Created RoomId: ", resp.json()['id'])  # You will need this roomId to post Messages to it
    return resp.json()['id']
    

def addMembers(roomId):
    message = '{"roomId":"' + roomId + '","personEmail": "test@test.com", "isModerator": false}'
    uri = 'https://api.ciscospark.com/v1/memberships'
    resp = requests.post(uri, data=message, headers=spark_header)
    print("SparkAPI: ", resp.json())


def postMsg(roomId,message):
    message = '{"roomId":"' + roomId + '","text":"'+message+'"}'
    uri = 'https://api.ciscospark.com/v1/messages'
    resp = requests.post(uri, data=message, headers=spark_header)
    print("SparkAPI: ", resp.json())


if __name__ == '__main__':
    setHeaders()
    room_id=createRoom("Brett's Room")
    addMembers(room_id)   # Passing roomId to members function here to Post Message.
    postMsg(room_id,"What's up World?")      # Passing roomId to message function here to Post Message.
    

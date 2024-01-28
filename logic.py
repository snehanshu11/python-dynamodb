import boto3
from boto3.dynamodb.conditions import Attr, Key
dd = boto3.resource('dynamodb')
table = dd.Table('UserPost')

def create_post(post:dict):
    response = table.put_item(
        Item = post
        )
    return response


def query_by_user_id(id:str):
    filter_exp = Key('user_id').eq(id)
    #filter_exp2 = Key('post_id').eq(id)
    response = table.query(KeyConditionExpression=filter_exp, ScanIndexForward=True)
    return response


def delete(id:str):
   response = table.delete_item(Key = {'user_id':'2','post_id':id}) 
   return response


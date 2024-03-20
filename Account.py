from Utils.Util import Util
import Character
import boto3


class Account:
    def __init__(self, username, password=None, salt=None, hash=None) -> None:
        self.username = username
        self.password = password
        self.salt = salt
        self.hash = hash

    def get_character(character_id):
        pass

    def save_to_database(self):
        dynamodb = boto3.resource('dynamodb')
        account_table = dynamodb.Table('MyQuest')
        account_table.put_item(
            Item={
                'Account ID': 2 ,
                'Username': self.username,
                'Salt': self.salt,
                'Hashed Password':  self.hash
            }
        )


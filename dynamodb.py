import boto3
import os
import getopt
import sys
from boto3.dynamodb.conditions import Key

def delete_item(upload_date, measurement_file):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table(os.getenv('DBPROCESS'))

	response = table.delete_item(
		Key = {
			'Date': upload_date, 
			'JsonData' : measurement_file
		}
	)
	item = response['item']
	print(item)
	
if __name__ == "__main__":
	try:
		opts,args = getopt.getopt(sys.argv[1:],"u:m:",["upload_date=","measurement_file="])
		upload_date = None
		measurement_file = None
		for option, arg in opts:
			if option in ('-u', '--upload_date'):
				upload_date = arg
			elif option in ('-m', '--measurement_file'):
				measurement_file = arg
		delete_item(upload_date, measurement_file)
	except Exception as e:
		print(e)
	
	
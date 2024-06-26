import boto3

# Crear un cliente para DynamoDB
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# # Crear la tabla
# response = dynamodb.create_table(
#     TableName='itm-daniel-cardona-2',
#     KeySchema=[
#         {
#             'AttributeName': 'id',
#             'KeyType': 'HASH'  # Clave de partición
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'id',
#             'AttributeType': 'S'  # S para String, N para Number, B para Binary
#         }
#     ],
#     BillingMode='PAY_PER_REQUEST'
# )

# print("Tabla creada:", response)

# eliminar la tabla
response = dynamodb.delete_table(
    TableName='itm-daniel-cardona-2'
)
import boto3

#crear cliente para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-daniel-cardona')

#leer un elemento de la tabla
#response = tabla.get_item(Key={'id':'2'})
#print(response['Item'])

#leer todos los elementos de la tabla
#response = tabla.scan()
#print(response['Items'])

#insertar elementos en una tabla
item = {
    'id': '3',
    'nombre': 'Camila',
    'ciudad': 'Sabaneta'
}

tabla.put_item(Item=item)

response = tabla.scan()
print(response['Items'])


#leer un elemento de la tabla
response = tabla.get_item(Key={'id':'3'})

print(response['Item'])

response = tabla.update_item(
    Key={
        'id': '3'  
    },
    UpdateExpression='SET nombre = :val1',  # Expresión de actualización

    ExpressionAttributeValues={

        ':val1': 'Camil'  # Nuevo valor para atributo2
    }
)
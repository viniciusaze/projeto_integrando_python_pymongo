import pymongo as pyM

password = input("Password: ")

# Connecting
client = pyM.MongoClient(f"mongodb+srv://ar-vinicius:{password}@cluster0.cx1y4t0.mongodb.net/"
                         f"?retryWrites=true&w=majority&appName=Cluster0")

db = client.test
collection = db["test_collection"]
print(collection)

# Creating post
posts = [{
    "client": "Vinícius Azevedo Rosso",
    "cpf": "03643545002",
    "address": "Rio Grande do Sul",
    "type_account": "Current",
    "agency": "00216505",
    "number_account": 886312,
    "balance": 567.98,
    "tags": ["Vinícius", "Rio Grande do Sul", "Current"]
        },
        {
    "client": "Gabriel Teixeira Fagundes",
    "cpf": "064874650",
    "address": "Paraná",
    "type_account": "Savings",
    "agency": "00216514",
    "number_account": 887801,
    "balance": 5650.0,
    "tags": ["Gabriel", "Paraná", "Savings"]
        },
        {
    "client": "Camila da Silva",
    "cpf": "874320654",
    "address": "Paraná",
    "type_account": "Current",
    "agency": "00214479",
    "number_account": 883320,
    "balance": 1487.82,
    "tags": ["Camila", "Paraná", "Current"]
        }]

# Submit data
posts_collection = db["posts"]
post_ids = posts_collection.insert_many(posts)


import random
from userDashboard import client

#testing the connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


data_base = client["traderstock"]
collection = data_base["traders"]

users = []
user1 = {"name":"Joe","Amount":100, "profit_loss/time":[]}


list_of_names = ["joe", "chris", "john", "prince", "stella",  "peter","james",
                 "rock", "phillip", "kola" ]
def add_users(usersName:list):
    #create the users and save them on mongo db
    for name in usersName:
        user = {"name":name, "amount":100, "profit_loss/time":[]}
        for i in range(60):
            profit_loss =random.uniform(-2, 2)
            user["profit_loss/time"].append((profit_loss, 1+i))

        users.append(user)

add_users(list_of_names)
print(users)

# collection.insert_many(users)
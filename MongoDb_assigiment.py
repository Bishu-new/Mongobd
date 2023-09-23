#!/usr/bin/env python
# coding: utf-8

# Ans 1 : MongoDB is an open-source document-oriented database that is designed to store a large scale of data and allows you to work with that data very efficiently. It is categorized under the NoSQL (Not only SQL) databases because the storage and retrieval of data in MongoDB are not in the form of tables1. Instead, MongoDB uses JSON-like documents with optional schemas.
# 
# Non-relational databases, often called NoSQL databases, are different from traditional relational databases in that they store their data in a non-tabular form45. Instead, non-relational databases might be based on data structures like documents4. This ability to digest and organize various types of information side by side makes non-relational databases much more flexible than relational databases.
# 
# MongoDB can be preferred over SQL databases in the following scenarios:
# 
# When your data is unstructured or complex, and there is no pre-determined schema.
# When you need to handle large amounts of data and store it as documents.
# When horizontal scaling or sharding is required.
# If you need to replicate SQL data to avoid costly queries in production.
# When you need to work with diverse data types and structures for modern applications.
# If your data may be changed frequently or for applications that handle many different kinds of data.
# When you need better performance, scalability, and flexibility.

# Ans 2 : MongoDB is a scalable, flexible NoSQL document database platform designed to overcome the limitations of relational databases and other NoSQL solutions. Here are some of its key features:
# 
# 1. **Document Model**: MongoDB is a document-oriented database, which means that data is stored as documents, and documents are grouped in collections¹. The document model is more natural for developers to work with because documents are self-contained and can be treated as objects.
# 
# 2. **Flexible Schema**: The documents in a single collection don't necessarily need to have exactly the same set of fields¹. This flexibility allows developers to iterate faster and migrate data between different schemas without any downtime.
# 
# 3. **Sharding**: Sharding is the process of splitting larger datasets across multiple distributed instances, or “shards”¹. When applied to particularly large datasets, sharding helps the database distribute and better execute what might otherwise be problematic and cumbersome queries.
# 
# 4. **Replication**: MongoDB supports Master Slave replication². A master can perform Reads and Writes and a Slave copies data from the master and can only be used for reads or back up (not writes).
# 
# 5. **Index Support**: Any field in the document can be indexed.
# 
# 6. **Ad-hoc Queries**: MongoDB supports ad-hoc queries and document-based queries.
# 
# 7. **Load Balancing**: It has an automatic load balancing configuration because of data placed in shards.
# 
# 8. **Server-side JavaScript execution**: MongoDB offers server-side JavaScript execution that makes it a user-friendly database.
# 
# 9. **High Performance**: MongoDB provides high performance for read and write operations.
# 
# 10. **Horizontal Scalability**: MongoDB is well known for its horizontal scaling and load balancing capabilities, which has given application developers an unprecedented level of flexibility and scalability.
# 
# 11. **Cloud-Based Developer Data Platform**: MongoDB Atlas is the leading global cloud database service for modern applications. Using Atlas, developers can deploy fully managed cloud databases across , Azure, and Google Cloud.

# Ans 3 : 

# In[9]:


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Pytonlearning:Bishu1994@cluster0.ozde5yd.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# In[13]:


db = client['pwskills']
coll_pwskills = db["my_record1"]


# Ans 4 :

# In[14]:


data = {"name" : "sudh" , 
        "class" :"data science masters " ,
        "time" : "flexi"}


# In[15]:


coll_pwskills.insert_one(data)


# In[16]:


data2 = [
  { "name": "Amy", "address": "Apple st 652" },
  { "name": "Hannah", "address": "Mountain 21" },
  { "name": "Michael", "address": "Valley 345" },
  { "name": "Sandy", "address": "Ocean blvd 2" },
  { "name": "Betty", "address": "Green Grass 1" },
  { "name": "Richard", "address": "Sky st 331" },
  { "name": "Susan", "address": "One way 98" },
  { "name": "Vicky", "address": "Yellow Garden 2" },
  { "name": "Ben", "address": "Park Lane 38" },
  { "name": "William", "address": "Central st 954" },
  { "name": "Chuck", "address": "Main Road 989" },
  { "name": "Viola", "address": "Sideway 1633" }
]


# In[17]:


coll_pwskills.insert_many(data2)


# In[18]:


coll_pwskills.find_one()


# In[20]:


for i in coll_pwskills.find():
    print(i) 


# Ans 5 : The find() method in MongoDB is a crucial part of MongoDB’s querying capabilities. It serves as the primary means to retrieve data from a collection1. It allows developers to perform read operations and fetch documents that match specific criteria or conditions

# In[21]:


#here is the simple code 
for i in coll_pwskills.find():
    print(i) 


# Ans 6: The `sort()` method in MongoDB is used to sort the documents in a collection¹². You can specify the order in which the query returns the matching documents from the given collection¹. The `sort()` method takes a document as a parameter that contains a field-value pair defining the sort order of the result set¹. The value is 1 or -1 specifying an ascending or descending sort respectively¹².
# 
# Here's an example of how you can use the `sort()` method to sort documents in a MongoDB collection:
# ```

# In[39]:


doc = coll_pwskills.find().sort("name" ,1)
for doc in doc:
    print(doc)


# In[ ]:





# Ans 7: The `delete_one()`, `delete_many()`, and `drop()` methods in MongoDB are used to remove data from a database[^10^]:
# 
# 1. **delete_one()**: The `delete_one()` method removes a single document from a collection¹. It deletes the first document that matches the filter¹. If there are multiple documents matching the filter query, only the first appeared document would be deleted⁴. For example, if you want to delete a document where the "name" field is "John", you would do: `db.collection.deleteOne({"name": "John"})`.
# 
# 2. **delete_many()**: The `delete_many()` method removes all documents that match the filter from a collection⁶. It deletes documents one at a time⁶. If you want to delete all documents where the "age" field is greater than 25, you would do: `db.collection.deleteMany({"age": {"$gt": 25}})`.
# 
# 3. **drop()**: The `drop()` method removes an entire collection from the database, including all of its documents and indexes. It returns true if the collection dropped successfully. For example, if you want to drop a collection named "Students", you would do: `db.Students.drop().
# 
# 

# In[ ]:





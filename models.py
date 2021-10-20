from pymongo import TEXT
from pymongo.operations import IndexModel
from pymodm import connect, fields, MongoModel, EmbeddedMongoModel

from datetime import datetime

connect("mongodb+srv://botaccessdb:NIuAaF7NAv9y2fcJ@cluster0.vufn3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

class ProductModel(MongoModel):
    productid = fields.CharField(primary_key=True, required=True)
    context = fields.CharField(required=True)
    desc = fields.CharField(required=False)

class SubscribtionProductModel(MongoModel):
    subscribtionid = fields.CharField(primary_key=True, required=True)
    product = fields.ReferenceField(ProductModel, required=True)
    periodweeks = fields.IntegerField(required=True)
    price = fields.FloatField(required=True)

class ActiveSubscribtionModel(EmbeddedMongoModel):
    id = fields.CharField(primary_key=True, required=True)
    subscribtion = fields.ReferenceField(SubscribtionProductModel, required=True)
    product = fields.ReferenceField(ProductModel, required=True)
    startdatetime = fields.DateTimeField(required=True)
    enddatetime = fields.DateTimeField(required=True)

class RequestPayment():
    def __init__(self):
        receiver: str = ""
        paymentTarget: str = ""
        amount: str = ""
        amount_due: str = ""
        paymentId: int = None
        transactionId: int = None
        storeName: str = ""
        productName: str = ""
        successURL: str = ""

class User(MongoModel):
    activeSubscriptions = fields.EmbeddedDocumentListField(ActiveSubscribtionModel, default=[])

    def checkActiveProduct(productName: str):
        return False
    def checkSubscribtionActive(subscribtionName: str):
        return False
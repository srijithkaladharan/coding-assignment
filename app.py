from flask import Flask
from resources.transaction import Transaction
from resources.transactionbyproducts import TransSummaryByProducts
from resources.transactionbycities import TransSummaryByCities
from flask_restful import Api
from appconfig import directory

app = Flask(__name__)

api = Api(app)

api.add_resource(Transaction, "/assignment/transaction/<int:transId>")
api.add_resource(
    TransSummaryByProducts, "/assignment/transactionSummaryByProducts/<int:n_days>"
)
api.add_resource(
    TransSummaryByCities, "/assignment/transactionSummaryByCities/<int:n_days>"
)

if __name__ == "__main__":
    try:
        app.run(port=8080, debug=True)
    except:
        print("Something went wrong!! Please try again..")

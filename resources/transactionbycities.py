from flask_restful import Resource
from models.transaction import TransactionModel
from time import sleep
from flask import stream_with_context, request, Response


class TransSummaryByCities(Resource):
    @classmethod
    def get(cls, n_days: int):
        def generate():
            while True:
                yield "<p>{}<p>".format(
                    TransactionModel.get_trans_summary_by_cities(n_days)
                )
                sleep(300)
                # since we assumed transaction file comes every 5mins, I have set the sleep to 300secs (5 * 60 = 300)

        return Response(stream_with_context(generate()))

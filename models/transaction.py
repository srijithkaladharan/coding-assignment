import csv
import os
from appconfig import directory
from datetime import datetime, timedelta


class TransactionModel:

    # to find the transaction details for a particular ID
    @classmethod
    def find_by_id(cls, id: int):
        files = cls.get_files()

        if len(files) != 0:
            for file_name in files:
                file_obj = open(directory["received"] + file_name)

                file_reader = list(csv.reader(file_obj))

                if (
                    int(file_reader[len(file_reader) - 1][0]) >= id
                    and int(file_reader[0][0]) <= id
                ):
                    element = cls.find_element_from_list(file_reader, id)
                    if element:
                        productId = element[1].lstrip()
                        prodName = cls.get_prod_name(productId)

                        return {
                            "transactionId": int(element[0]),
                            "productName": prodName,
                            "transactionAmount": float(element[2]),
                            "transactionDatetime": element[3].lstrip(),
                        }

            return {"message": "Transaction with id:" + str(id) + " not found."}
        return {"message": "Sorry! We do not have any transaction data."}

    # to get transaction summary by products
    @classmethod
    def get_trans_summary_by_prods(cls, days_count: int):
        files = cls.get_files()
        summary = {}

        if len(files) != 0:
            for file_name in files:
                file_obj = open(directory["received"] + file_name)
                file_reader = csv.reader(file_obj)

                for row in file_reader:
                    transactTime = datetime.strptime(
                        row[3].lstrip(), "%Y-%m-%d %H:%M:%S"
                    )
                    givenTime = datetime.today() - timedelta(days=days_count)
                    if transactTime >= givenTime:
                        if row[1] in summary.keys():
                            summary[row[1]] = summary[row[1]] + float(row[2])
                        else:
                            summary[row[1]] = float(row[2])

            if len(summary.keys()) > 0:
                finalSummary = {"summary": []}

                for key in summary.keys():
                    prodId = key.lstrip()
                    prodName = cls.get_prod_name(prodId)

                    finalSummary["summary"].append(
                        {"productName": prodName, "totalAmount": summary[key]}
                    )
                return finalSummary
            return {
                "message": "There is no summary data for last "
                + str(days_count)
                + " days."
            }
        return {"message": "Sorry!, We do not have any transaction data"}

    # to get transaction summary by products
    @classmethod
    def get_trans_summary_by_cities(cls, n_days):
        summary_by_prod = cls.get_trans_summary_by_prods(n_days)
        if "summary" not in summary_by_prod.keys():
            return summary_by_prod
        summary_by_prod = summary_by_prod["summary"]

        prodSummaryDict = {}

        for prod in summary_by_prod:
            prodSummaryDict[prod["productName"]] = prod["totalAmount"]

        citySummaryDict = {}

        prod_obj = open(directory["reference"] + "products.csv")
        prod_reader = csv.reader(prod_obj)
        for eachProd in prod_reader:
            prodName = eachProd[1].lstrip()
            if prodName in prodSummaryDict.keys():
                city = eachProd[2].lstrip()
                if city in citySummaryDict.keys():
                    citySummaryDict[city] = (
                        citySummaryDict[city] + prodSummaryDict[prodName]
                    )
                else:
                    citySummaryDict[city] = prodSummaryDict[prodName]
        finalSummary = {"summary": []}
        for key in citySummaryDict.keys():
            finalSummary["summary"].append(
                {"cityName": key, "totalAmount": citySummaryDict[key]}
            )

        return finalSummary

    # to get the list of files from the landing directory where we receive the files from the source
    @classmethod
    def get_files(cls):
        files = os.listdir(directory["received"])
        return files

    # to get the product name from static reference
    @classmethod
    def get_prod_name(cls, prodId):
        prod_obj = open(directory["reference"] + "products.csv")
        prod_reader = csv.reader(prod_obj)

        for eachProd in prod_reader:
            if eachProd[0] == prodId:
                return eachProd[1].lstrip()

    @classmethod
    def find_element_from_list(cls, elementList, checkVal):
        start = 0
        last = len(elementList) - 1

        while start <= last:
            mid = start + (last - start) // 2
            midVal = int(elementList[mid][0])
            if midVal == checkVal:
                return elementList[mid]
            elif midVal < checkVal:
                start = mid + 1
            else:
                last = mid - 1

        return False


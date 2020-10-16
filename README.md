# coding-assignment
Interview Coding Assignment

By Srijith Kaladharan | Email : srijithkaladharan1002@gmail.com |

Please find the application setup procedure given below. I have also shared it on email as attachment.

1) Assuming that python is installed on your machine.

2) Open Terminal/Command Prompt.

3) Clone the code repository - (command) -> git clone https://github.com/srijithkaladharan/coding-assignment.git

4) Create and activate a python virtual environment (reference link) -> https://docs.python.org/3/tutorial/venv.html

5) Move into the project directory (command) -> cd coding-assignment

6) Install the required python packages/libraries

Run the below mentioned commands (Check if the newly created virtual environment is activated)

pip install flask

pip install flask-restful

7) Run the application (command) -> python app.py

The application will run on http://127.0.0.1:8080/

-------------------------------------------------------------------------------------------

Available API end points:

1) http://127.0.0.1:8080/assignment/transaction/{transaction_id}

2) http://127.0.0.1:8080/assignment/transactionSummaryByProducts/{last_n_days}

3) http://127.0.0.1:8080//assignment/transactionSummaryByCities/{last_n_days

-------------------------------------------------------------------------------------------

data-file directory structure:

data-file/received/   -> Landing Directory where the incoming files from upstream/source systems would reside.
data-file/refrence/   -> Contains the static reference file (Products.csv)

--------------------------------------------------------------------------------------------

data file naming convention - transact + "-" + yyyymmdd + "-" + hhmm + ".csv"

Example- transact-20201016-1000.csv is a data file received on 16-OCT-2020 at 10:00 hours


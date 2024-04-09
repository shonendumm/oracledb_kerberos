
## Feature summary of python-oracledb and cx_oracle
https://python-oracledb.readthedocs.io/en/latest/user_guide/appendix_a.html#featuresummary



To use python-oracledb with Kerberos credentials, you need to have the Oracle Instant Client and Oracle Wallet Manager installed on your system. Here's a step-by-step guide on how to set this up:

## Install Oracle Instant Client:
- Download the Oracle Instant Client ZIP file from the Oracle website for your operating system.
- Extract the contents of the ZIP file to a directory on your system.
- Add the Instant Client directory to the PATH environment variable.

## Configure Oracle Wallet Manager:
Run the Oracle Wallet Manager and create a new wallet.
Import the Kerberos Keytab file into the wallet.
Configure the wallet to use the Kerberos authentication method.

## Install python-oracledb:
Install the python-oracledb package using pip:
pip install cx_Oracle

## Configure the connection in your Python script:
Use the following code snippet as a template for connecting to the Oracle database with Kerberos credentials:

import cx_Oracle

dsn = cx_Oracle.makedsn('<hostname>', '<port>', service_name='<service_name>')
conn = cx_Oracle.connect('<username>', '', dsn, encoding='UTF-8', mode=cx_Oracle.SYSDBA, kerberos=True)
Replace <hostname>, <port>, <service_name>, and <username> with your database connection details.

## Test the connection:
Run your Python script to test the connection to the Oracle database using Kerberos credentials.
If the connection is successful, you should be able to execute SQL queries and interact with the database.
# To connect to an Oracle database using Kerberos credentials, you need to follow these steps:

# Install the Oracle client on your machine.
# Configure Kerberos. This involves creating a krb5.conf file with the details of your Kerberos server.
# Configure the Oracle client to use Kerberos. This involves creating a sqlnet.ora file and possibly a tnsnames.ora file with the details of your Oracle server.
# Obtain a Kerberos ticket using the kinit command.
# Use the Oracle client to connect to the Oracle server.


import os
import platform
import oracledb

# Set the Oracle environment variables. See https://python-oracledb.readthedocs.io/en/stable/user_guide/initialization.html#oracle-environment-variables-for-python-oracledb-thick-mode 
# It is recommended to set Oracle variables in the environment before calling Python. 
# Alternatively, use os.putenv() before the first connection is established. 
os.environ['ORACLE_HOME'] = '/usr/lib/oracle/21/client64'
os.environ['TNS_ADMIN'] = '/usr/lib/oracle/21/client64/network/admin' # directory containing the tnsnames.ora or sqlnet.ora file

# System environment variables like LD_LIBRARY_PATH must be set before Python starts.
# Example in makefile:
# export LD_LIBRARY_PATH=/usr/lib/oracle/21/client64/lib # directory containing the Oracle client libraries
# or export LD_LIBRARY_PATH="/usr/lib/oracle/21/client64/lib"


# Initialize the Oracle client library
oracle_instant_client = None  # default suitable for Linux
if platform.system() == "Windows":
  oracle_instant_client = os.environ.get("ORACLE_CLIENT_LIB_DIR") or r"C:\oracle\instantclient_19_18" # address to the instant client, use raw string to avoid escape characters \U, \n, etc.
oracledb.init_oracle_client(lib_dir=oracle_instant_client)


# Connect to the Oracle database using Kerberos credentials
dsn = """
(DESCRIPTION=
    (ADDRESS=(PROTOCOL=TCP)(HOST=example.com)(PORT=1521))
    (CONNECT_DATA=
        (SERVICE_NAME=servicename) 
    )
)
"""
# SERVICE_NAME=servicename, Specifies the service name of the Oracle database.
# Note: Make sure to replace example.com and servicename, or port(?).

connection = oracledb.connect(
    dsn=dsn,
    kerberos=True,
    # encoding='UTF-8',  # Optionally specify the character encoding
    # encoding_errors='strict'  # Optionally specify how encoding errors should be handled
)

# Create a cursor object
cursor = connection.cursor()

# Execute a query
cursor.execute('SELECT * FROM table_name')

# Fetch the results
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()


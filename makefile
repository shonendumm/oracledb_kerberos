# Makefile for running a Flask Python app with LD_LIBRARY_PATH set

# Define path to Python interpreter within virtual environment
VENV_DIR = /path/to/your/venv
PYTHON = $(VENV_DIR)/bin/python

# Define directory containing Oracle client libraries
ORACLE_LIB_DIR = /usr/lib/oracle/21/client64/lib

# Define environment variables / := simply expanded now. = recursively expanded later ?= simply expanded if not already set
export LD_LIBRARY_PATH := $(ORACLE_LIB_DIR)

# Define target to run the Flask app
run:
    $(PYTHON) app.py


# use make run in the terminal to run the Flask app
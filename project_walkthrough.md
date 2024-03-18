#Install with Pip
Create a directory for your agents related project: mkdir directory_name

Within the directory, create and open a virtual environment using Poetry: poetry init -n && poetry shell

Install Fetch.ai uAgents Framework: pip install uagents

Check if installation was successful: pip show uagents

# Walk-through
First of all, we need to navigate towards the directory you created for your project and create a folder for this task: mkdir booking_demo.

Inside this folder we will create another folder for our protocols: mkdir protocols.

After having defined our protocols, we will create 2 scripts, one for our restaurant and the other one for user agents. These agents will make use of the protocols to query, check, confirm and book an available table at the restaurant.

We can start by writing the code for our 2 protocols.


# Protocols
Table querying protocol
Let's start by defining the protocol for querying availability of tables at the restaurant:

First of all, we need to navigate towards the protocols folder: cd protocols

Let's then create a Python script and name it by running: touch query.py

In the text editor application, we proceed and define the table querying protocol.

We now need to import necessary classes and define the message data models. Then, create an instance of the Protocol class and name it query_proto:

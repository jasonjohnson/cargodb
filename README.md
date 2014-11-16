CargoDB
=======
A simple document-oriented database.

Notes
-----
* Client is educated about all potential storage nodes
* Client attempts to create database 'example-db'
    * nodes = ['a', 'b', 'c']
    * node = crc32('example-db') % len(nodes)
    * node = -1598054313 % 3
    * node = 0
    * db_create('example-db') on nodes[node]

Storage Server Commands
-----------------------
Possible commands to produce tasks:
* db-fetch <database-id>\n
* db-init <database-id>\n
* db-delete <database-id>\n
* doc-fetch <database-id> <document-id>\n
* doc-init <database-id> <document-id>\n
* doc-save <database-id> <document-id> <content>\n
* doc-delete <database-id> <document-id>\n

Possible responses:
* [<document-id>,<document-id>,...]
* <content>\n
* ok\n
* error\n

database-id: a-zA-Z0-9_-
document-id: a-zA-Z0-9_-
content: newline-terminated

TODO
----
* Support responses to operations
* Construct basic client
* Serialize tasks across worker threads
* Serialize operations based on target database
* Start more than one worker thread


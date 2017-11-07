### proj6-mongo ###

### Author: Shohei Etzel
### email: sse@uoregon.edu

### Summary ###
Simple list of dated memos kept in MongoDB database.
All users access the same database. Users can insert memos
 which display in a manner relative to the current time.
User also can remove any memo they like at any time.

### Testing(Changes made) ###
From the main repository, type the command "run test" to run tests using nose. I have changed the Makefile so it runs tests in a similar fashion to project 4.
Note: PLEASE RUN THE TESTS ON AN EMPTY MEMO DATABASE

### Running server ###
From the main repository, type the command "run make". This will begin the server and the server will begin running on the specified port. (e.g. on my computer port 5000). The debugger will also display the running port if you are unsure.

### Stopping server ###
Nothing is specified in our makefile to stop the server, so simply type ctrl+c to quit server.


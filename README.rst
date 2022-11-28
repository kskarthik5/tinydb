
TinyDB consists of a table module which is responsible for executing operations on tables in a database. Following are the changes which were done to each of the table functions -


	def operation(args):

	    writeToLog() # Change 1. writing in the log file that this operation is under execution

	    check() # Change 2. check function which checks for errors in the log file and also performs recovery
		.... #actual execution of operation

	    appendToLogRecord() # Change 3. marking log record as done(D)

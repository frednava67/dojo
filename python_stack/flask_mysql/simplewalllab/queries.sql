use simplewalldb;

select * from messages WHERE toaccount_id = 3 order by created_at;

select * from accounts;

#get all messages sent to a particular person
SELECT * from messages
JOIN accounts ON accounts.id=messages.fromaccount_id
WHERE toaccount_id = 3;

#get all messages from a particular person
SELECT * from messages
JOIN accounts ON accounts.id=messages.toaccount_id
WHERE fromaccount_id = 3;

#get total number of messages sent from user
SELECT COUNT(*) from messages
JOIN accounts ON accounts.id=messages.toaccount_id
WHERE fromaccount_id = 3;

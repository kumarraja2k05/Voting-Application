DELIMITER //
CREATE PROCEDURE DelVoteRecord()
BEGIN
	delete from VoteRecord where user_id!=-1;
END //
DELIMITER ;
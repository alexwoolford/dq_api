# create databases
CREATE DATABASE IF NOT EXISTS `db_api`;
CREATE DATABASE IF NOT EXISTS `test_dq_api`;

# create root user and grant rights
CREATE USER 'db_api'@'%' IDENTIFIED BY 'V1ctoria';
GRANT ALL ON *.* TO 'db_api'@'%';

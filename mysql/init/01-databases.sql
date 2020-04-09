# create databases
CREATE DATABASE IF NOT EXISTS `dq_api`;
CREATE DATABASE IF NOT EXISTS `test_dq_api`;

# grant rights
GRANT ALL ON *.* TO 'dq_api'@'%';

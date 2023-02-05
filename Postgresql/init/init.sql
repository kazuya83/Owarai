--DBの作成
CREATE DATABASE domain;
GRANT ALL PRIVILEGES ON DATABASE domain TO nwriter;
\c domain

CREATE TABLE T_Group (
    group_id SERIAL,
    group_unique_name VARCHAR(2000) NOT NULL,
    group_name VARCHAR(2000) NOT NULL,
    craete_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    create_user_id INTEGER DEFAULT 1,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_user_id INTEGER DEFAULT 1,
    is_deleted BOOL DEFAULT '0',
    PRIMARY KEY(group_id)
);

CREATE TABLE T_Group_User (
    group_id INT NOT NULL,
    group_user_seq SERIAL,
    gropu_user_unique_name VARCHAR(2000) NOT NULL,
    group_user_name VARCHAR(2000) NOT NULL,
    create_user_id INTEGER DEFAULT 1,
    update_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    update_user_id INTEGER DEFAULT 1,
    is_deleted BOOL DEFAULT '0',
    PRIMARY KEY(group_id, gropu_user_unique_name)
);
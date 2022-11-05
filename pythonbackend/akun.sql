CREATE TABLE akun(
    id int not null auto_increment, 
    username varchar(75) not null, 
    email varchar(85) not null,
    password varchar(75),
    waktu_buat datetime default current_timestamp,
    primary key(id)
)
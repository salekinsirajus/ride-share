create table if not exists users
(
        uid serial primary key,
        name varchar(50)
);

create table if not exists trips
(
        tid serial primary key,
        --uid doesn't exist
        uid serial,
        origin varchar(50),
        destination varchar(50),
        dateEarly date,
        dateLate date,
        price money,
        foreign key (uid) references users(uid)
);

create table if not exists passengers
(
        pid serial primary key,
        --changing uid and tid to serial from int
        tid serial,
        uid serial,
        foreign key (tid) references trips(tid),
        foreign key (uid) references users(uid)
);

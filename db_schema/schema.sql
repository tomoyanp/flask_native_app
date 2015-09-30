drop table if exists blog_table;
create table blog_table (
    id integer primary key autoincrement,
    entry_id string not null,
    entry_day string not null,
    title string not null,
    first_genre string not null,
    second_genre string not null,
    third_genre string not null,
    fab_count int default 0
);

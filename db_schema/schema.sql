drop table if exists blog_table;
create table blog_table (
    id integer primary key autoincrement,
    title string not null,
    entry_day date not null,
    contents string not null
);

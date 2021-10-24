CREATE TABLE IF NOT EXISTS books
(
    id                 bigint primary key not null,
    author_fullname    text,
    title_original     text,
    collapse_parent_id bigint,
    is_collection      boolean,
    collapse_id        bigint,
    parent_id          bigint,
    publication_type   text,
    norm_part          int
);

DO
$$
    BEGIN
        CREATE TYPE event_enum AS enum ('add', 'create_order', 'issue');
    EXCEPTION
        WHEN duplicate_object THEN null;
    END
$$;

CREATE TABLE IF NOT EXISTS history
(
    user_id    bigint     not null,
    book_id    bigint     not null,
    event      event_enum not null,
    created_on date
);

CREATE INDEX history_index ON history (user_id, book_id);

CREATE TABLE IF NOT EXISTS recsys_predictions
(
    user_id    bigint,
    book_id    bigint,
    prediction real
);

CREATE TABLE IF NOT EXISTS recsys_popular
(
    book_id bigint,
    rating  bigint primary key
);


COPY recsys_predictions (
                         user_id,
                         book_id,
                         prediction
    )
    FROM '/var/datasets/recsys_predictions.csv'
    DELIMITER ','
    CSV HEADER;

COPY books (id,
            author_fullname,
            title_original,
            collapse_parent_id,
            is_collection,
            collapse_id,
            parent_id,
            publication_type,
            norm_part)
    FROM '/var/datasets/books_prepared.csv'
    DELIMITER ','
    CSV HEADER;

COPY history (
              user_id,
              book_id,
              event,
              created_on
    )
    FROM '/var/datasets/history_prepared.csv'
    DELIMITER ','
    CSV HEADER;

COPY recsys_popular (
              book_id,
              rating
    )
    FROM '/var/datasets/recsys_popular.csv'
    DELIMITER ','
    CSV HEADER;

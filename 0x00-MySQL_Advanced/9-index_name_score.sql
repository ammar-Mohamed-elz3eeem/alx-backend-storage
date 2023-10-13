-- create index from name and score combined

CREATE INDEX idx_name_first_score ON names (name(1), score);

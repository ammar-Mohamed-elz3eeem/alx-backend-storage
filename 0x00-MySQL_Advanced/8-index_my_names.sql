-- Create index for the first charchter in name

CREATE INDEX idx_name_first ON names (name(1));

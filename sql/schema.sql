-- Dimension Tables
CREATE TABLE dim_programs (
    program_id INT PRIMARY KEY,
    program_name TEXT,
    budget NUMERIC,
    start_year INT
);

CREATE TABLE dim_beneficiaries (
    beneficiary_id INT PRIMARY KEY,
    region TEXT,
    gender TEXT,
    age_group TEXT
);

-- Fact Tables
CREATE TABLE fact_donations (
    donation_id INT PRIMARY KEY,
    donor_type TEXT,
    region TEXT,
    amount NUMERIC,
    donation_year INT
);

CREATE TABLE fact_expenses (
    expense_id SERIAL PRIMARY KEY,
    program_id INT,
    expense_type TEXT,
    expense_amount NUMERIC,
    FOREIGN KEY (program_id) REFERENCES dim_programs(program_id)
);

CREATE TABLE fact_program_participation (
    program_id INT,
    beneficiary_id INT,
    completion_status TEXT,
    FOREIGN KEY (program_id) REFERENCES dim_programs(program_id),
    FOREIGN KEY (beneficiary_id) REFERENCES dim_beneficiaries(beneficiary_id)
);

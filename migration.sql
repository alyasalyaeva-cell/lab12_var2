-- Таблица пациентов
CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    oms_policy VARCHAR(16) UNIQUE NOT NULL,
    birth_date DATE NOT NULL,
    email VARCHAR(100) NOT NULL,
    gender VARCHAR(10) NOT NULL
);

CREATE INDEX ix_patients_full_name ON patients (full_name);

-- Таблица приемов (Для Задания 9)
CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(id),
    doctor_id INTEGER NOT NULL,
    visit_date DATE NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
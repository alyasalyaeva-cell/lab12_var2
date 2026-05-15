SELECT doctor_id, COUNT(id) as visit_count
FROM appointments
WHERE visit_date >= CURRENT_DATE - INTERVAL '1 month'
GROUP BY doctor_id
ORDER BY visit_count DESC
LIMIT 3;
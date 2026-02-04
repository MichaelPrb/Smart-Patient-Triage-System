-- =========================================================
-- CASE 2: High Risk Patient Analysis
-- Objective: Identify patients in Neurology with high symptom complexity.
-- Risk Criteria: Age > 50 AND Symptom Count >= 3
-- =========================================================

SELECT
    p.name AS patient_name,
    p.age AS patient_age,
    v.visit_date,
    COUNT(s.id) AS symptom_count
FROM
    patients p
JOIN
    visits v ON p.id = v.patient_id
JOIN
    symptoms s ON v.id = s.visit_id
WHERE
    v.department = 'Neurology'      -- Focus on Neurology department
    AND p.age > 50                  -- Age risk factor
GROUP BY
    p.id, p.name, p.age, v.id, v.visit_date
HAVING
    COUNT(s.id) >= 3                -- Complexity risk factor (3+ symptoms)
ORDER BY
    v.visit_date DESC               -- Show latest visits first
LIMIT 5;
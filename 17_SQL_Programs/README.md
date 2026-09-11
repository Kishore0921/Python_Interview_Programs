# 17_SQL_Programs

This folder is part of a personal collection of materials created for
**practicing interview coding problems**. Unlike the Python-based
folders in this collection, this one is **explanation-only** — each
`.sql` file uses SQL comments to walk through a topic conceptually, with
illustrative syntax and examples, rather than a runnable script against
a live database.

## Contents

| # | File | Description |
|---|------|-------------|
| 1 | `basic_queries.sql` | CREATE TABLE, INSERT, SELECT, UPDATE, DELETE |
| 2 | `select_where.sql` | WHERE, logical operators, BETWEEN, IN, LIKE, NULL checks, ORDER BY, LIMIT |
| 3 | `joins.sql` | INNER, LEFT, RIGHT, FULL, SELF, and CROSS joins |
| 4 | `group_by.sql` | Aggregate functions, GROUP BY, HAVING, and clause execution order |
| 5 | `subqueries.sql` | Subqueries in WHERE/FROM/SELECT, IN, EXISTS, and correlated subqueries |
| 6 | `constraints.sql` | NOT NULL, UNIQUE, PRIMARY KEY, FOREIGN KEY, CHECK, DEFAULT, AUTO_INCREMENT |

## Format

Each file follows a consistent structure using SQL comments (`--`):

1. A **Topic** header describing what the file covers.
2. The file is divided into **numbered sections**, one per concept,
   separated by comment banners.
3. Each section includes:
   - A plain-language explanation of the concept
   - The general **syntax**
   - A concrete, illustrative **example**
4. A closing note on **why the topic matters in interviews**.

Example format used throughout:

```sql
-- ------------------------------------------------------------
-- 1. INNER JOIN
-- ------------------------------------------------------------
-- Returns only the rows where there is a match in BOTH tables.
--
-- Syntax:
--   SELECT columns
--   FROM table1
--   INNER JOIN table2 ON table1.column = table2.column;
--
-- Example:
--   SELECT employees.name, departments.department_name
--   FROM employees
--   INNER JOIN departments ON employees.department_id = departments.id;
```

No runnable schema or seed data is included — the goal is to build a
clear conceptual reference for each topic, using a small set of
consistent example tables (`employees`, `departments`) throughout.

## How to Use

These files are meant to be read, not executed. Open any `.sql` file in
an editor to review the concept, syntax, and examples. If you want to
practice hands-on, you can copy the example statements into any SQL
environment (e.g. SQLite, MySQL, PostgreSQL, or an online SQL sandbox)
and adapt them to a real table you've created.

## Purpose

This folder is meant purely for **interview preparation practice** — SQL
questions are extremely common in technical interviews across data,
backend, and full-stack roles, and understanding these six topics
(basic CRUD, filtering, joins, aggregation, subqueries, and constraints)
covers the large majority of SQL questions asked in practice.
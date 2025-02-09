# ETL Pipeline

##  Pasos

1. Generación de datos sintéticos (`generate_data.py`): se crean datasets de clientes, pólizas, reclamaciones y factores de riesgo. Los campos de cada uno de los datasets se han escogido de forma aleatoria sin tener mucho conocimiento del área. Los valores generados se han obtenido en la mayoría de casos de forma aleatoria por lo que esto influirá en la calidad de los datos.
2. Ingesta de datos (`data_processing.py`): se cargan los datos desde archivos JSON a pandas.
3. Limpieza de los datos y transformación: se eliminan duplicados, se rellenan valores nulos y se estandarizan los datos.
4. Cargar los datos a postgreSQL: se almacenan los datos en la base de datos.

## Limpieza de datos y transformación

En este paso se han hecho algunas asumpciones respecto a qué decisiones tomar a la hora de limpiar los datos.

- Valores nulos en datos categóricos: se reemplazan por "unknown".
- Fechas nulas o mal formateadas: se convierten a `datetime` y los valores nulos se reemplazan por `2020-01-01`.
- Valores numéricos: se convierten a `float`y los nulos se reemplazan por la media de la columna.
- Duplicados: se eliminan.
- Todas las `string` se transforman a minúscula.

## Esquema de la base de datos

A continuación se presentan los esquemas de cada una de las tablas en la base de datos:

Table "public.customers"

|     Column     |            Type             |
|----------------|-----------------------------|
| customer_id    | text                        |
| customer_name  | text                        |
| date_of_birth  | timestamp without time zone |
| phone_number   | text                        |
| email          | text                        |
| street_address | text                        |
| state          | text                        |
| post_code      | text                        |
| iban           | text                        |
| job            | text                        |

Table "public.policies"

|   Column    |            Type             |
|-------------|-----------------------------|
| policy_id   | text                        |
| customer_id | text                        |
| policy_type | text                        |
| created_at  | timestamp without time zone |

 Table "public.claims"

|   Column    |            Type             |
|-------------|-----------------------------|
| claim_id    | text                        |
| customer_id | text                        |
| policy_id   | text                        |
| claim_date  | timestamp without time zone |

Table "public.risk_indicators"

|       Column        |       Type       |
|---------------------|------------------|
| customer_id         | text             |
| driving_violations  | double precision |
| property_risk_score | double precision |
| health_risk_score   | double precision |

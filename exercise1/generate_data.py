import random
import json
from faker import Factory

fake = Factory.create("es_ES")


def generate_customers(n):
    customers_data = []
    customer_ids = []

    for _ in range(n):
        customer_id = f"C-{fake.uuid4()}"
        customer_ids.append(customer_id)

        customers_data.append(
            {
                "customer_id": customer_id,
                "customer_name": fake.name(),
                "date_of_birth": fake.date_of_birth().isoformat(),
                "phone_number": fake.phone_number(),
                "email": fake.email(),
                "street_address": fake.street_address(),
                "state": fake.state(),
                "post_code": fake.postcode(),
                "iban": random.choices([fake.iban(), None], weights=[0.9, 0.1])[0],
                "job": fake.job(),
            }
        )
    return customers_data, customer_ids


def generate_policies(customer_ids, max_policies=3, min_policies=1):
    policies_data = []
    policy_ids = []

    for customer_id in customer_ids:
        num_policies = random.randint(min_policies, max_policies)
        for _ in range(num_policies):
            policy_id = f"P-{fake.uuid4()}"
            policy_ids.append((customer_id, policy_id))

            policies_data.append(
                {
                    "policy_id": policy_id,
                    "customer_id": customer_id,
                    "policy_type": random.choice(
                        [
                            "house",
                            "car",
                            "health",
                            "pet",
                            None,
                        ]
                    ),
                    "created_at": random.choices(
                        [
                            fake.date_between(start_date="-10y").isoformat(),
                            None,
                        ],
                        weights=[0.9, 0.1],
                    )[0],
                }
            )
    return policies_data, policy_ids


def generate_claims(policy_ids, max_claim_per_policy=10):
    claims_data = []

    for policy_id, customer_id in policy_ids:
        num_claims = random.randint(0, max_claim_per_policy)
        for _ in range(num_claims):
            claims_data.append(
                {
                    "claim_id": f"CL-{fake.uuid4()}",
                    "customer_id": customer_id,
                    "policy_id": policy_id,
                    "claim_date": random.choices(
                        [
                            fake.date_between(start_date="-10y").isoformat()
                            ,
                            None,
                        ],
                        weights=[0.9, 0.1],
                    )[0],
                }
            )
    return claims_data


def generate_risk_indicators(customer_ids):
    risk_indicators_data = []

    for customer_id in customer_ids:
        risk_indicators_data.append(
            {
                "customer_id": customer_id,
                "driving_violations": random.choices(
                    [random.randint(0, 10), None], weights=[0.9, 0.1]
                )[0],
                "property_risk_score": round(random.uniform(0, 10), 2),
                "health_risk_score": random.choices(
                    [round(random.uniform(0, 10), 2), None], weights=[0.9, 0.1]
                )[0],
            }
        )
    return risk_indicators_data


def save_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    customers, customer_ids = generate_customers(50)

    data_dir = "data"
    save_json(customers, f"{data_dir}/customers.json")

    policies, policy_ids = generate_policies(customer_ids)
    save_json(policies, f"{data_dir}/policies.json")

    claims = generate_claims(policy_ids)
    save_json(claims, f"{data_dir}/claims.json")

    risk_indicators = generate_risk_indicators(customer_ids)
    save_json(risk_indicators, f"{data_dir}/risk_indicators.json")

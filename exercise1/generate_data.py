import random
import json
from faker import Factory
import os

fake = Factory.create("es_ES")


def generate_customers(n):
    # generates fake customer data

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
                # add some null values
                "iban": random.choices([fake.iban(), None], weights=[0.9, 0.1])[0],
                "job": fake.job(),
            }
        )
    return customers_data, customer_ids


def generate_policies(customer_ids, max_policies=3, min_policies=1):
    # generate fake policies data
    # for each customer, generate from 1 to 3 policies
    policies_data = []
    policy_info = []

    for customer_id in customer_ids:
        num_policies = random.randint(min_policies, max_policies)
        for _ in range(num_policies):
            policy_id = f"P-{fake.uuid4()}"
            policy_creation_date = fake.date_between(start_date="-5y")
            policy_info.append((customer_id, policy_id, policy_creation_date))

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
                            policy_creation_date.isoformat(),
                            None,
                        ],
                        weights=[0.9, 0.1],
                    )[0],
                }
            )
    return policies_data, policy_info


def generate_claims(policy_info):
    #generate fake claims data for each policy-customer pair

    claims_data = []

    for customer_id, policy_id, policy_creation_date in policy_info:
        num_claims = random.choices(
            [0, 1, 2, 3, 4, 5],
            weights=[0.65, 0.15, 0.10, 0.05, 0.03, 0.02],
        )[0]
        for _ in range(num_claims):
            claims_data.append(
                {
                    "claim_id": f"CL-{fake.uuid4()}",
                    "customer_id": customer_id,
                    "policy_id": policy_id,
                    "claim_date": random.choices(
                        [
                            fake.date_between(start_date=policy_creation_date).isoformat(),
                            None,
                        ],
                        weights=[0.9, 0.1],
                    )[0],
                }
            )
    return claims_data


def generate_risk_indicators(customer_ids):
    # generate fake risk indicators for each customer
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
    # generate the different datasets
    customers, customer_ids = generate_customers(500)
    policies, policy_ids = generate_policies(customer_ids)
    claims = generate_claims(policy_ids)
    risk_indicators = generate_risk_indicators(customer_ids)

    data_dir = "data"
    # check if the folder exists
    if not os.path.exists(data_dir):
        # create the folder if it does not exist
        os.makedirs(data_dir)
        print(f"Folder '{data_dir}' created.")

    # save datasets into json files
    save_json(customers, f"{data_dir}/customers.json")
    save_json(policies, f"{data_dir}/policies.json")
    save_json(claims, f"{data_dir}/claims.json")
    save_json(risk_indicators, f"{data_dir}/risk_indicators.json")

class ClientRegistration:
    data = {
        "firstname": "Albert",
        "lastname": "Smith",
        "street_address_1": "700 Fortt St",
        "street_address_2": "Suite 300",
        "city": "Victoria",
        "state": "BC",
        "zip_code": "V8X 1X1",
        "phone": "250-123-4567",
        "email": "albert.smith@email.com",
        "comment": "Hi there!"
        }

    expected_text = data["firstname"] + ", " + data["lastname"]


class ClientOnBoarding:
    data = {"phone": "250-222-3434", "slack_email": "slack@email.com", "your_email": "youremail@email.com",
            "social_media_logins": "facebook@email.com, instagram@email.com, twitter@email.com"}
    expected_text = data["your_email"]


class Marketing:
    data = {"firstname": "Rita", "lastname": "Baker", "email": "albert.smith@email.com",
            "company" : "R B Ltd", "phone": "250-123-4567", "describe": "All Products :)"}
    expected_text = data["firstname"] + ", " + data["lastname"]


class Users:
    names = ["Emma", "Olivia", "Ava", "Isabella", "Sophia", "Charlotte", "Mia", "Amelia", "Harper", "Evelyn",
             "Liam", "Noah", "William", "James", "Oliver", "Benjamin", "Elijah", "Lucas", "Mason", "Logan",
             "Genesis", "Saint", "Baker", "Kairo", "Watson", "Kenzo", "Jaxtyn", "Kylo", "Dakari", "Karsyn",
             "Genesis", "Saint", "Baker", "Kairo", "Watson", "Kenzo", "Jaxtyn", "Kylo", "Dakari","Karsyn"]

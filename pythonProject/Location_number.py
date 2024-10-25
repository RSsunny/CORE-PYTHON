import phonenumbers
from phonenumbers import geocoder, carrier

# Example phone number (in international format)
phone_number = "+8801755766682"  # Replace with the phone number you want to check

# Parse the phone number
parsed_number = phonenumbers.parse(phone_number)

# Get location (country/region)
location = geocoder.description_for_number(parsed_number, "en")

# Get the carrier (telecom provider)
service_provider = carrier.name_for_number(parsed_number, "en")

# Output the information
print(f"Location: {location}")
print(f"Service Provider: {service_provider}")


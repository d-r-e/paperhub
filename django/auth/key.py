import jwt
import time


def generate_jwt(app_id, pem_file_path):
    # Read the private key from the .pem file
    with open(pem_file_path, "r") as pem_file:
        private_key = pem_file.read()

    # Create the JWT payload
    payload = {
        # Issued at time
        "iat": int(time.time()),
        # JWT expiration time (10 minutes maximum)
        "exp": int(time.time()) + (10 * 60),
        # GitHub App's identifier
        "iss": app_id,
    }

    # Create the JWT
    jwt_token = jwt.encode(payload, private_key, algorithm="RS256")
    return jwt_token

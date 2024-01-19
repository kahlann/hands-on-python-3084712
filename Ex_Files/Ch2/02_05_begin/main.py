import os

# Define variables for environments
DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

# Get the current environment - if no environment name, take the default value (second argument, DEVELOPMENT)
current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

# Report which environment we're in
if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")

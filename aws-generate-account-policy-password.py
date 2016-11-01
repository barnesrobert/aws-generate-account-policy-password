#==================================================================================================
# function: generate_temporary_password
# purpose:  generates a temporary password that complies with the account settings.
#==================================================================================================
def generate_temporary_password():

    # Get the account's policy.
    policy = boto3.client("iam").get_account_password_policy()

    # Define the allowable symbols.
    # http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_account-policy.html
    SYMBOLS = "!@#$%^&*()_+-=[]{}|'"

    # We need to ensure that we meet the minimum length while still ensuring that,
    # of that required length, we include the required characters.
    reserved_length_for_required_characters = 0
    if policy["PasswordPolicy"]["RequireLowercaseCharacters"]: reserved_length_for_required_characters += 1
    if policy["PasswordPolicy"]["RequireUppercaseCharacters"]: reserved_length_for_required_characters += 1
    if policy["PasswordPolicy"]["RequireNumbers"]: reserved_length_for_required_characters += 1
    if policy["PasswordPolicy"]["RequireSymbols"]: reserved_length_for_required_characters += 1

    # Get the maximun number of chracacters. Subtract the number reserved for special characters, 
    # because we'll manually insert those. Then add 2 for over-achievement.
    length = int(policy["PasswordPolicy"]["MinimumPasswordLength"]) - reserved_length_for_required_characters + 2

    # Generate the initial password before inserting special characaters. If we insert required characters first,
    # then those characters would always be in the same order.    
    password = "".join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + SYMBOLS) for _ in range(length))

    # Now ensure we meet the character requirements by inserting the appropriate value.
    if policy["PasswordPolicy"]["RequireLowercaseCharacters"]:
        password = insert_character(password, "".join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(1)))

    if policy["PasswordPolicy"]["RequireUppercaseCharacters"]:
        password = insert_character(password, "".join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(1)))

    if policy["PasswordPolicy"]["RequireNumbers"]:
        password = insert_character(password, "".join(random.SystemRandom().choice(string.digits) for _ in range(1)))

    if policy["PasswordPolicy"]["RequireSymbols"]:
        password = insert_character(password, "".join(random.SystemRandom().choice(SYMBOLS) for _ in range(1)))

    return password


#==================================================================================================
# function: insert_character
# purpose:  inserts a required character in a random location in the given string.
#==================================================================================================
def insert_character(string, character):
    
    # Convert the string to a list...
    string = list(string)

    # ...get a random position in the string...
    random_position = random.randrange(len(string)-1)

    # ...insert the character there...
    string[random_position] = string[random_position] + character

    # ...then return the result.
    return ''.join(string)
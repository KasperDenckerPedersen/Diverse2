import re

#email = input("Email: ")
email = 'jdoe@hr.company.com'
email_list = ['jdoe@hr.company.com', 'dahae@it.company.com', 'kabcve@mkt.company.com', 'vacve@hr.company.com', 'vagh@it.company.com', 'vljjh@ops.company.com', 'caajjh@mkt.company.com']

checker = re.compile("([a-z]){1}([a-z]+)@(hr|it|fin|mkt|ops)\.company\.com")

def validate_email(email):
    m = checker.match(email)

    if m:
        print("The email is valid")
    else:
        print("The email is not valid")

def get_department(email):
    m = checker.match(email)
    if m:
        print(m.group(3))
    else:
        print(f"{email} is not valid")

def catagorize_emails(email_list):
    categorized_emails = {"hr": [], "it": [], "fin": [], "mkt": [], "ops": []}
    for email in email_list:
        m = checker.match(email)
        if m: 
            if m.group(3) == "hr":
                categorized_emails["hr"].append(email)
            if m.group(3) == "it":
                categorized_emails["it"].append(email)
            if m.group(3) == "fin":
                categorized_emails["fin"].append(email)
            if m.group(3) == "mkt":
                categorized_emails["mkt"].append(email)
            if m.group(3) == "ops":
                categorized_emails["ops"].append(email)
        else:
            print(f"{email} is not valid")
    return categorized_emails

# 1
print("1:")
validate_email(email)

# 2
print("2:")
get_department(email)

# 3
print("3:")
categorized_emails = catagorize_emails(email_list)
print(categorized_emails)
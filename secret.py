def getSecret(name):

    secrets_path = r"C:\Users\Benjamin\Documents\Flask\secrets.txt"
    with open(secrets_path, 'r') as secrets_id:
        secrets_file = secrets_id.readlines()
        for line in secrets_file:
            if name in line:
                return line.split(':')[1][:-1]

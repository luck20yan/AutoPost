import yaml

yaml_file = open("config.yaml", 'r')
yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

if yaml_content['telegram']:
    if not yaml_content['telegram']['token']:
        print("ERROR: no telegram token")
        exit(1)
    if not yaml_content['telegram']['channel']:
        print("ERROR: no telegram channel id")
        exit(1)
    telegram_token = yaml_content['telegram']['token']
    telegram_channel = yaml_content['telegram']['channel']
if yaml_content['twitter']:
    if not yaml_content['twitter']['consumer_key']:
        print("ERROR: no twitter consumer_key")
        exit(1)
    if not yaml_content['twitter']['consumer_secret']:
        print("ERROR: no twitter consumer_secret")
        exit(1)
    if not yaml_content['twitter']['access_token']:
        print("ERROR: no twitter access_token")
        exit(1)
    if not yaml_content['twitter']['access_token_secret']:
        print("ERROR: no twitter access_token_secret")
        exit(1)
    consumer_key = yaml_content['twitter']['consumer_key']
    consumer_secret = yaml_content['twitter']['consumer_secret']
    access_token = yaml_content['twitter']['access_token']
    access_token_secret = yaml_content['twitter']['access_token_secret']
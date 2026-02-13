import requests
from yaml import safe_dump, safe_load
from config import PIXELA_URL, config_dict


def save_yaml(file_name: str, d: dict):
    try:
        with open(file_name, 'w') as file:
            safe_dump(d, file)
    except IOError as e:
        print(f"Error saving creds: {e}")


def create_user_account(token: str,
                        user_name: str):
    user_params = {
        "token": token,
        "username": user_name,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"}
    response = requests.post(url=PIXELA_URL, json=user_params)
    print(response.text)
    creds = {'token': token,
             'user_name': user_name}
    save_yaml(config_dict['creds_file_name'], creds)


def create_graph(graph_id: str,
                 graph_name: str):
    creds = read_pixela_creds()
    graph_params = {
        "id": graph_id,
        "name": graph_name,
        "unit": "reps",
        "type": "int",
        "color": "sora"
    }
    graph_endpoint = f"{PIXELA_URL}{creds['user_name']}/graphs/"
    response = requests.post(url=graph_endpoint, json=graph_params, headers=creds['headers'])
    creds['graph_id'] = graph_id
    creds["graph_endpoint"] = f"{graph_endpoint}{graph_id}"
    save_yaml(config_dict['creds_file_name'], creds)
    print(response.text)


def read_pixela_creds():
    with open(config_dict['creds_file_name'], "r") as f:
        # contains: url, token
        pixela = safe_load(f)
    pixela["headers"] = {"X-USER-TOKEN": pixela['token']}
    return pixela

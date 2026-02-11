import requests
import webbrowser
from yaml import safe_load


def read_pixela_creds(file):
    with open(file, "r") as f:
        # contains: url, token
        pixela = safe_load(f)
    pixela["graph_endpoint"] = f"https://pixe.la/v1/users/{pixela['user_name']}/graphs/{pixela['graph_name']}.html"
    pixela["header"] = {"X-USER-TOKEN": pixela["token"]}
    return pixela


def attempt_to_add_pixel(date, reps):
    pixela_creds = read_pixela_creds('pixela_creds_andrea.yaml')
    pixel_params = {
        "date": str(date),
        "quantity": str(reps)
    }
    response = requests.post(url=pixela_creds['graph_endpoint'], json=pixel_params, headers=pixela_creds['header'])
    return response


def add_pixel(date, reps, max_attempts=10):
    success = False
    num_attempts = 0
    while success is False and num_attempts <= max_attempts:
        response = attempt_to_add_pixel(date, reps=reps)
        num_attempts += 1
        print(response)
        if response.status_code == 200:
            success = True
    # webbrowser.open("https://pixe.la/v1/users/andreality/graphs/pushups.html")

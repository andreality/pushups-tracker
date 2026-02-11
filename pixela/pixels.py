import requests
import webbrowser
from pixela.setup import read_pixela_creds


def attempt_to_add_pixel(date, reps, url, headers):
    pixela_params = {
        "date": str(date),
        "quantity": str(reps)
    }
    response = requests.post(url=url, json=pixela_params, headers=headers)
    return response


def add_pixel(date, reps, max_attempts=10):
    pixela_creds = read_pixela_creds()
    success = False
    num_attempts = 0
    while success is False and num_attempts <= max_attempts:
        response = attempt_to_add_pixel(date,
                                        reps=reps,
                                        url=pixela_creds['graph_endpoint'],
                                        headers=pixela_creds['headers'])
        num_attempts += 1
        print(response)
        if response.status_code == 200:
            success = True
    webbrowser.open(f"{pixela_creds['graph_endpoint']}.html")

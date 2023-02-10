import requests


def send_request(url, method='GET', query_params=None, body_params=None, header_params=None):
    if query_params:
        url = url + '?' + '&'.join([f'{key}={value}' for key, value in query_params.items()])

    if method == 'GET':
        response = requests.get(url, headers=header_params)
    elif method == 'POST':
        response = requests.post(url, json=body_params, headers=header_params)
    elif method == 'PUT':
        response = requests.put(url, json=body_params, headers=header_params)
    elif method == 'DELETE':
        response = requests.delete(url, headers=header_params)
    else:
        raise ValueError(f'Invalid HTTP method: {method}')

    if response.status_code not in range(200, 299):
        return None

    return response

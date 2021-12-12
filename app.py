#!/usr/bin/env python3

from flask import Flask, render_template

STATUS_CODES = {
    200: 'OK',
    404: 'Not Found',
    418: 'I\'m a teapot',
    500: 'Internal Server Error'
}

SERVICES = [
    {
        'url': 'alfa.xyz',
        'status': 200
    },
    {
        'url': 'bravo.xyz',
        'status': 404
    },
    {
        'url': 'charlie.xyz',
        'status': 500
    },
    {
        'url': 'delta.xyz',
        'status': 418
    }
]

def get_services():
    services = []

    for service in SERVICES:
        url = service.get('url')
        status = service.get('status')
        notes = STATUS_CODES.get(status, '')

        services.append({
            'url': url,
            'status': status,
            'notes': notes
        })

    return services

APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def do_get():
    services = get_services()
    return render_template('index.html', services=services)

if __name__ == '__main__':
    APP.run()

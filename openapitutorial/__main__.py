import connexion


def setup_app():
    app = connexion.FlaskApp(
        'openapitutorial',
        host='0.0.0.0',
        port=10080,
        specification_dir='apispec/',
        debug=True,
        options={
            'swagger_ui': True,
        },
    )
    app.add_api(
        'v1/openapi.yaml',
        validate_responses=True,
    )
    return app


if __name__ == '__main__':
    app = setup_app()
    app.run()

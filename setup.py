from setuptools import setup

setup(
    name='jupyterhub-jwtauthenticator-oauth-logout',
    version='0.0.1',
    description='JSONWebToken Authenticator for JupyterHub with override for LogoutHandler endpoint',
    url='https://github.com/izihawa/jwtauthenticator_v2',
    author='Dan Quintero',
    author_email='dquintero@ata-llc.com',
    license='Apache 2.0',
    packages=['jwtauthenticator'],
    install_requires=[
        'jupyterhub',
        'pyjwt',
    ]
)

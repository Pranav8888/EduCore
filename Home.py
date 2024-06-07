import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title="EduCore",
    page_icon="📙",
    layout = "wide"
)

st.title("EDUCORE")

config = {
    'credentials': {
        'usernames': {
            'johndoe': {
                'name': 'John Doe',
                'password': 'abc'
            },
            'janedoe': {
                'name': 'Jane Doe',
                'password': 'def'
            }
        }
    },
    'cookie': {
        'expiry_days': 30,
        'key': 'some_signature_key',
        'name': 'some_cookie_name'
    },
    'preauthorized': {
        'emails': []
    }
}

# Save configuration to a file
with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)

# Load configuration from the file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create an authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, auth_status, user_name = authenticator.login()

if auth_status:
    authenticator.logout()
elif auth_status is False:
    st.error('Username/password is incorrect')
elif auth_status is None:
    st.warning('Please enter your username and password')
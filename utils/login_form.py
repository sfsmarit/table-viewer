import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


def login() -> bool:
    config_yaml = 'config.yaml'

    with open(config_yaml) as f:
        config = yaml.load(f, Loader=SafeLoader)

    pre_auth_status = st.session_state.get('authentication_status', None)

    authenticator = stauth.Authenticate(
        config['credentials'],
        cookie_name=config['cookie']['name'],
        key=config['cookie']['key'],
        cookie_expiry_days=config['cookie']['expiry_days'],
    )

    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    post_auth_status = st.session_state['authentication_status']

    # ログイン画面を消すために再実行する
    if not pre_auth_status and post_auth_status:
        st.rerun()

    if st.session_state["authentication_status"]:
        return True
    elif st.session_state["authentication_status"] is False:
        st.error("Username or password is incorrect")

    with open(config_yaml, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

    return False

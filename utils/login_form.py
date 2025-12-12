import streamlit as st
import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


def login() -> bool:
    """
    Perform user authentication using Streamlit and streamlit-authenticator, persist
    the credential configuration, and indicate success as a boolean.

    The function reads authentication settings from ``config.yaml``, renders a login
    form via ``streamlit-authenticator``, and updates ``st.session_state`` with the
    authentication result. On the first successful login (i.e., a transition from
    unauthenticated to authenticated), the app is re-run to remove the login form
    from the UI. The (potentially) modified configuration is then written back to
    ``config.yaml``.

    Parameters
    ----------
    None

    Returns
    -------
    bool
        ``True`` if the user is authenticated (``st.session_state["authentication_status"]`` is truthy),
        otherwise ``False``.

    Raises
    ------
    Exception
        Any exception raised during the call to ``authenticator.login()`` is caught and
        displayed via ``st.error(e)``. The exception is not re-raised.

    Side Effects
    ------------
    - Reads from ``config.yaml`` and writes to it at the end of the function.
    - Updates ``st.session_state["authentication_status"]`` via streamlit-authenticator.
    - Calls ``st.rerun()`` when a new successful login occurs to remove the login form.
    - Displays errors in the Streamlit UI using ``st.error(...)``.

    Notes
    -----
    - The configuration is loaded using ``yaml.SafeLoader`` and dumped with ``yaml.dump(...)``
      enabling Unicode and disabling flow style.
    - A false authentication status triggers an error message: ``"Username or password is incorrect"``.
    - The function assumes the following structure in ``config.yaml``:
      ``credentials`` and ``cookie`` keys with nested fields:
      ``cookie.name``, ``cookie.key``, and ``cookie.expiry_days``.
    - ``pre_auth_status`` and ``post_auth_status`` are compared to detect a transition
      from not authenticated to authenticated; when detected, ``st.rerun()`` is invoked.

    Examples
    --------
    >>> # In a Streamlit app file:
    >>> import streamlit as st
    >>> from login_form import login
    >>>
    >>> if not login():
    ...     st.stop()
    >>> st.write("Welcome to the dashboard.")
    """

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

    # When successfully authenticated, rerun the app to delete login form
    if not pre_auth_status and post_auth_status:
        st.rerun()

    if st.session_state["authentication_status"]:
        return True
    elif st.session_state["authentication_status"] is False:
        st.error("Username or password is incorrect")

    with open(config_yaml, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

    return False

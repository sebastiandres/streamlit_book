import streamlit as st

def add_floating_button(url, bootstrap_icon, icon_color, background_color):
    """
    Adds a floating button that opens a link to feedback.
    """
    url_html = f'<a href="{url}" target="_blank"><i class="bi {bootstrap_icon}"></i></a>'
    button_html = """
        <link rel="stylesheet" 
              href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
        <style>
        i.bi {
            position: fixed;
            right: 10px;
            bottom: 50px;
            background: my_background_color;
            color: my_color;
            border-radius: 30%;
            text-align: center;
            vertical-align: middle;
            padding: 10px;
            }
        </style>
        my_url
    """
    button_html = button_html.replace("my_background_color", background_color)
    button_html = button_html.replace("my_color", icon_color)
    button_html = button_html.replace("my_url", url_html)
    st.components.v1.html(button_html, height=100)
    return url, bootstrap_icon, icon_color, background_color

def make_it_float(url, bootstrap_icon, icon_color, background_color):
    # Define your javascript
    my_js = """
    var containers = window.parent.document.querySelectorAll('.element-container');
    for (var i = 0; i < containers.length; i++) {
        //alert(i);
        let container = containers[i];
        let child = container.firstChild
        let name = child.tagName;
        if (name == 'IFRAME') {
            let docsrc = child.srcdoc;
            bool1 = docsrc.includes('my_url');
            bool2 = docsrc.includes('my_bootstrap_icon');
            bool3 = docsrc.includes('my_icon_color');
            bool4 = docsrc.includes('my_background_color');
            if (bool1 && bool2 && bool3 && bool4) {
                child.style.position = "fixed";
                child.style.bottom = "10px";
                child.style.right = "10px";
                child.style.zindex = "2000";
            }
        }
    }
    """
    my_js = my_js.replace("my_url", url)
    my_js = my_js.replace("my_bootstrap_icon", bootstrap_icon)
    my_js = my_js.replace("my_icon_color", icon_color)
    my_js = my_js.replace("my_background_color", background_color)
    # Wrapt the javascript as html code
    my_html = f"<script>{my_js}</script>"
    # Execute your app
    st.components.v1.html(my_html, height=0, width=2000)

def floating_button(url, bootstrap_icon="chat-left-text-fill", 
                        icon_color="white", background_color="gray"):
    """
    """
    # Fix bootstrap icon if does not starts with "bi"
    if not bootstrap_icon.startswith("bi-"):
        bootstrap_icon = "bi-" + bootstrap_icon
    # Wrapt the javascript as html code
    properties = add_floating_button(url, bootstrap_icon, icon_color, background_color)
    make_it_float(*properties)
    return
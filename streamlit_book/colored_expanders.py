import streamlit as st

def add_color_to_expanders():
    """
    Adds color to the expanders.
    Users don't need to call this function, is executed by default.
    """
    # Define your javascript
    my_js = """
    // Define the colors
    const color_dict = {
                    "info": ["#EAF2FC", "#1D6777"],
                    "success": ["#D7EED9", "#156C36"],
                    "ok": ["#D7EED9", "#156C36"],
                    "warning": ["#FFF4D9", "#947C2D"],
                    "error": ["#FFDDDC", "#9D282C"]
                    };
    // Get all the expander elements
    var expanderHeaders = window.parent.document.querySelectorAll('.streamlit-expanderHeader');
    var expanderContents = window.parent.document.querySelectorAll('.streamlit-expanderContent');
    for (var i = 0; i < expanderHeaders.length; i++) {
        let header = expanderHeaders[i];
        let content = expanderContents[i];
        text = header.innerText || header.textContent;
        // Check for text content
        for (let color in color_dict) {
            if (text.toLowerCase().startsWith(color)) {
                header.style.backgroundColor = color_dict[color][0];
                content.style.backgroundColor = color_dict[color][0];
                header.style.color = color_dict[color][1];
                content.style.color = color_dict[color][1];
                header.addEventListener("mouseover", function(event){header.style.color = 'red'})
                header.addEventListener("mouseout", function( event ) {header.style.color = color_dict[color][1]})
            }
        }
    }    
    """

    # Wrapt the javascript as html code
    my_html = f"<script>{my_js}</script>"

    # Execute your app
    st.components.v1.html(my_html, height=0, width=0)

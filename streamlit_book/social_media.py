from streamlit.components.v1 import html

def share(my_url, my_text):
    """
    This function takes a url and a text and displays
    clickable sharing buttons in html.
    This is based on https://sharingbuttons.io/
    By large the simplest and best way to share the content. Kudos to creator.

    :param my_url: the url to share on social media
    :type my_url: str
    :param my_text: the text to share on social media
    :type my_text: str
    """

    # Define the css style for the sharing buttons
    my_css = """
    .resp-sharing-button__link,
    .resp-sharing-button__icon {
        display: inline-block
    }

    .resp-sharing-button__link {
        text-decoration: none;
        color: #fff;
        margin: 0.5em
    }

    .resp-sharing-button {
        border-radius: 5px;
        transition: 25ms ease-out;
        padding: 0.5em 0.75em;
        font-family: Helvetica Neue,Helvetica,Arial,sans-serif
    }

    .resp-sharing-button__icon svg {
        width: 1em;
        height: 1em;
        margin-right: 0.4em;
        vertical-align: top
    }

    .resp-sharing-button--small svg {
        margin: 0;
        vertical-align: middle
    }

    /* Non solid icons get a stroke */
    .resp-sharing-button__icon {
        stroke: #fff;
        fill: none
    }

    /* Solid icons get a fill */
        .resp-sharing-button__icon--solid,
        .resp-sharing-button__icon--solidcircle {
        fill: #fff;
        stroke: none
    }

    .resp-sharing-button--twitter {
        background-color: #55acee
    }

    .resp-sharing-button--twitter:hover {
        background-color: #2795e9
    }

    .resp-sharing-button--pinterest {
        background-color: #bd081c
    }

    .resp-sharing-button--pinterest:hover {
        background-color: #8c0615
    }

    .resp-sharing-button--facebook {
        background-color: #3b5998
    }

    .resp-sharing-button--facebook:hover {
        background-color: #2d4373
    }

    .resp-sharing-button--tumblr {
        background-color: #35465C
    }

    .resp-sharing-button--tumblr:hover {
        background-color: #222d3c
    }

    .resp-sharing-button--reddit {
        background-color: #5f99cf
    }

    .resp-sharing-button--reddit:hover {
        background-color: #3a80c1
    }

    .resp-sharing-button--google {
        background-color: #dd4b39
    }

    .resp-sharing-button--google:hover {
        background-color: #c23321
    }

    .resp-sharing-button--linkedin {
        background-color: #0077b5
    }

    .resp-sharing-button--linkedin:hover {
        background-color: #046293
    }

    .resp-sharing-button--email {
        background-color: #777
    }

    .resp-sharing-button--email:hover {
        background-color: #5e5e5e
    }

    .resp-sharing-button--xing {
        background-color: #1a7576
    }

    .resp-sharing-button--xing:hover {
        background-color: #114c4c
    }

    .resp-sharing-button--whatsapp {
        background-color: #25D366
    }

    .resp-sharing-button--whatsapp:hover {
        background-color: #1da851
    }

    .resp-sharing-button--hackernews {
        background-color: #FF6600
    }
    .resp-sharing-button--hackernews:hover, .resp-sharing-button--hackernews:focus {   background-color: #FB6200 }

    .resp-sharing-button--vk {
        background-color: #507299
    }

    .resp-sharing-button--vk:hover {
        background-color: #43648c
    }

    .resp-sharing-button--facebook {
        background-color: #3b5998;
        border-color: #3b5998;
    }

    .resp-sharing-button--facebook:hover,
    .resp-sharing-button--facebook:active {
        background-color: #2d4373;
        border-color: #2d4373;
    }

    .resp-sharing-button--twitter {
        background-color: #55acee;
        border-color: #55acee;
    }

    .resp-sharing-button--twitter:hover,
    .resp-sharing-button--twitter:active {
        background-color: #2795e9;
        border-color: #2795e9;
    }

    .resp-sharing-button--email {
        background-color: #777777;
        border-color: #777777;
    }

    .resp-sharing-button--email:hover,
    .resp-sharing-button--email:active {
        background-color: #5e5e5e;
        border-color: #5e5e5e;
    }

    .resp-sharing-button--linkedin {
        background-color: #0077b5;
        border-color: #0077b5;
    }

    .resp-sharing-button--linkedin:hover,
    .resp-sharing-button--linkedin:active {
        background-color: #046293;
        border-color: #046293;
    }

    .resp-sharing-button--whatsapp {
        background-color: #25D366;
        border-color: #25D366;
    }

    .resp-sharing-button--whatsapp:hover,
    .resp-sharing-button--whatsapp:active {
        background-color: #1DA851;
        border-color: #1DA851;
    }

    .resp-sharing-button--telegram {
        background-color: #54A9EB;
    }

    .resp-sharing-button--telegram:hover {
        background-color: #4B97D1;}
    """

    # Define the html
    my_html = f"""
    <!-- Sharingbutton Facebook -->
    <span>
        <a class="resp-sharing-button__link" href="https://facebook.com/sharer/sharer.php?u={my_url}" target="_blank" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--facebook resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0C5.38 0 0 5.38 0 12s5.38 12 12 12 12-5.38 12-12S18.62 0 12 0zm3.6 11.5h-2.1v7h-3v-7h-2v-2h2V8.34c0-1.1.35-2.82 2.65-2.82h2.35v2.3h-1.4c-.25 0-.6.13-.6.66V9.5h2.34l-.24 2z"/></svg>
            </div>
        </div>
        </a>

        <!-- Sharingbutton Twitter -->
        <a class="resp-sharing-button__link" href="https://twitter.com/intent/tweet/?text={my_text}&amp;url={my_url}" target="_blank" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--twitter resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0C5.38 0 0 5.38 0 12s5.38 12 12 12 12-5.38 12-12S18.62 0 12 0zm5.26 9.38v.34c0 3.48-2.64 7.5-7.48 7.5-1.48 0-2.87-.44-4.03-1.2 1.37.17 2.77-.2 3.9-1.08-1.16-.02-2.13-.78-2.46-1.83.38.1.8.07 1.17-.03-1.2-.24-2.1-1.3-2.1-2.58v-.05c.35.2.75.32 1.18.33-.7-.47-1.17-1.28-1.17-2.2 0-.47.13-.92.36-1.3C7.94 8.85 9.88 9.9 12.06 10c-.04-.2-.06-.4-.06-.6 0-1.46 1.18-2.63 2.63-2.63.76 0 1.44.3 1.92.82.6-.12 1.95-.27 1.95-.27-.35.53-.72 1.66-1.24 2.04z"/></svg>
            </div>
        </div>
        </a>

        <!-- Sharingbutton E-Mail -->
        <a class="resp-sharing-button__link" href="mailto:?subject={my_text}&amp;body={my_url}" target="_self" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--email resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 0C5.38 0 0 5.38 0 12s5.38 12 12 12 12-5.38 12-12S18.62 0 12 0zm8 16c0 1.1-.9 2-2 2H6c-1.1 0-2-.9-2-2V8c0-1.1.9-2 2-2h12c1.1 0 2 .9 2 2v8z"/><path d="M17.9 8.18c-.2-.2-.5-.24-.72-.07L12 12.38 6.82 8.1c-.22-.16-.53-.13-.7.08s-.15.53.06.7l3.62 2.97-3.57 2.23c-.23.14-.3.45-.15.7.1.14.25.22.42.22.1 0 .18-.02.27-.08l3.85-2.4 1.06.87c.1.04.2.1.32.1s.23-.06.32-.1l1.06-.9 3.86 2.4c.08.06.17.1.26.1.17 0 .33-.1.42-.25.15-.24.08-.55-.15-.7l-3.57-2.22 3.62-2.96c.2-.2.24-.5.07-.72z"/></svg>
            </div>
        </div>
        </a>

        <!-- Sharingbutton LinkedIn -->
        <a class="resp-sharing-button__link" href="https://www.linkedin.com/shareArticle?mini=true&amp;url={my_url}&amp;title={my_text}&amp;summary={my_text}&amp;source={my_url}" target="_blank" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--linkedin resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg version="1.1" x="0px" y="0px" width="24px" height="24px" viewBox="0 0 24 24" enable-background="new 0 0 24 24" xml:space="preserve">
                <path d="M12,0C5.383,0,0,5.383,0,12s5.383,12,12,12s12-5.383,12-12S18.617,0,12,0z M9.5,16.5h-2v-7h2V16.5z M8.5,7.5 c-0.553,0-1-0.448-1-1c0-0.552,0.447-1,1-1s1,0.448,1,1C9.5,7.052,9.053,7.5,8.5,7.5z M18.5,16.5h-3V13c0-0.277-0.225-0.5-0.5-0.5 c-0.276,0-0.5,0.223-0.5,0.5v3.5h-3c0,0,0.031-6.478,0-7h3v0.835c0,0,0.457-0.753,1.707-0.753c1.55,0,2.293,1.12,2.293,3.296V16.5z" />
            </svg>
            </div>
        </div>
        </a>

        <!-- Sharingbutton WhatsApp -->
        <a class="resp-sharing-button__link" href="https://wa.me/?text={my_text}%20{my_url}" target="_blank" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--whatsapp resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg xmlns="http://www.w3.org/2000/svg" height="24" width="24" viewBox="0 0 24 24"><path d="m12 0c-6.6 0-12 5.4-12 12s5.4 12 12 12 12-5.4 12-12-5.4-12-12-12zm0 3.8c2.2 0 4.2 0.9 5.7 2.4 1.6 1.5 2.4 3.6 2.5 5.7 0 4.5-3.6 8.1-8.1 8.1-1.4 0-2.7-0.4-3.9-1l-4.4 1.1 1.2-4.2c-0.8-1.2-1.1-2.6-1.1-4 0-4.5 3.6-8.1 8.1-8.1zm0.1 1.5c-3.7 0-6.7 3-6.7 6.7 0 1.3 0.3 2.5 1 3.6l0.1 0.3-0.7 2.4 2.5-0.7 0.3 0.099c1 0.7 2.2 1 3.4 1 3.7 0 6.8-3 6.9-6.6 0-1.8-0.7-3.5-2-4.8s-3-2-4.8-2zm-3 2.9h0.4c0.2 0 0.4-0.099 0.5 0.3s0.5 1.5 0.6 1.7 0.1 0.2 0 0.3-0.1 0.2-0.2 0.3l-0.3 0.3c-0.1 0.1-0.2 0.2-0.1 0.4 0.2 0.2 0.6 0.9 1.2 1.4 0.7 0.7 1.4 0.9 1.6 1 0.2 0 0.3 0.001 0.4-0.099s0.5-0.6 0.6-0.8c0.2-0.2 0.3-0.2 0.5-0.1l1.4 0.7c0.2 0.1 0.3 0.2 0.5 0.3 0 0.1 0.1 0.5-0.099 1s-1 0.9-1.4 1c-0.3 0-0.8 0.001-1.3-0.099-0.3-0.1-0.7-0.2-1.2-0.4-2.1-0.9-3.4-3-3.5-3.1s-0.8-1.1-0.8-2.1c0-1 0.5-1.5 0.7-1.7s0.4-0.3 0.5-0.3z"/></svg>
            </div>
        </div>
        </a>

        <!-- Sharingbutton Telegram -->
        <a class="resp-sharing-button__link" href="https://telegram.me/share/url?text={my_text}&amp;url={my_url}" target="_blank" rel="noopener" aria-label="">
        <div class="resp-sharing-button resp-sharing-button--telegram resp-sharing-button--small"><div aria-hidden="true" class="resp-sharing-button__icon resp-sharing-button__icon--solidcircle">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 23.5c6.35 0 11.5-5.15 11.5-11.5S18.35.5 12 .5.5 5.65.5 12 5.65 23.5 12 23.5zM2.505 11.053c-.31.118-.505.738-.505.738s.203.62.513.737l3.636 1.355 1.417 4.557a.787.787 0 0 0 1.25.375l2.115-1.72a.29.29 0 0 1 .353-.01L15.1 19.85a.786.786 0 0 0 .746.095.786.786 0 0 0 .487-.573l2.793-13.426a.787.787 0 0 0-1.054-.893l-15.568 6z" fill-rule="evenodd"/></svg>
            </div>
        </div>
        </a>
    </span>
    """

    # Define button html
    my_share_button = f"""
    <style>
    {my_css}
    </style>
    {my_html}
    """

    # Render
    html(my_share_button)

    return
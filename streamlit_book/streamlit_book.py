import streamlit as st
from glob import glob
from .render import render_file

## Next button not working
#if "page" not in st.session_state:
#    st.session_state.page = 0

#def on_next_click():
#    st.session_state.page += 1

def get_items(path: str, counter=0):
    """
    # Search for folders, python files or markdown files.
    Only looks at precisely the level of the given path.
    It returns a dictionary, with keys the name to be rendered in the selectbox
    and with values another dictionary, with the type (file/folder) and the fullpath.
    """
    # Get all the files
    items_at_path = glob(f"{path}/*/") + glob(f"{path}/*.md") + glob(f"{path}/*.py")
    # Filter files that start with WIP (work in progress)
    items_at_path = [item for item in items_at_path if ("/WIP" not in item)]
    # Create
    item_dict = {}
    for i, my_item in enumerate(items_at_path):
        counter = counter + i + 1
        if my_item[-3:] in (".py", ".md"):
            item_name = my_item.split("/")[-1]
            render_name = item_name[:-3]
            item_dict[render_name] = {"type":"file", "path":my_item, "counter":counter}
        else:
            item_name = my_item.split("/")[-2]
            render_name = item_name
            item_dict[render_name] = {"type":"folder", "path":my_item, "counter":counter}
    return item_dict

def set_book_config(path: str):
    """
    Renders a dynamically filled sidebar with selectboxes, allowing
    the user to select a file that gets displayed on the main view.
    It uses recursion to navigate though the folder selections until
    reaching a file that can be render.
    """
    # Depth counter, naming convention for content (depending on depth), 
    # and a wrapper function to call it more easily
    depth = 1
    book_convention_dict = {1:"section", 2:"chapter", 3:"subchapter", 4:"content"}
    book_naming = lambda n: book_convention_dict[min(n, len(book_convention_dict))]
    # Get the items (files/folders) at path level
    items_at_path_dict = get_items(path=path)
    # Provide a select box for user to select, if not an empty list:
    if len(items_at_path_dict)>0:
        selected_item = st.sidebar.selectbox(f"Select {book_naming(depth)}:", 
                                            options=sorted(items_at_path_dict.keys()),
                                            key=f"select_box_{depth}")
        item_dict = items_at_path_dict[selected_item]
        # Depending on selection, render if file or procede recursively
        while item_dict["type"]!="file" or len(items_at_path_dict)==0:
            depth += 1
            items_at_path_dict = get_items(item_dict["path"])
            # Provide the select box for current items
            if len(items_at_path_dict)>0:
                selected_item = st.sidebar.selectbox(f"Select {book_naming(depth)}:", 
                                                    options=sorted(items_at_path_dict.keys()),
                                                    key=f"select_box_{depth}")
                item_dict = items_at_path_dict[selected_item]
            else:
                break
        # Render the file, if we got one!
        if item_dict["type"]=="file":
            st.caption(item_dict["path"])
            render_file(fullpath=item_dict["path"])
            #st.button("Next", on_click=on_next_click)
        else:
            st.warning("Empty folder")
    else:
        st.error("The provided path is completely empty!")
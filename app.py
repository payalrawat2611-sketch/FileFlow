import streamlit as st
from pathlib import Path
import os

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="FileFlow",
    page_icon="📂",
    layout="wide"
)

# ----------------------------
# CSS
# ----------------------------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#0f172a,#1e293b,#111827);
color:white;
}

.big-title{
font-size:55px;
font-weight:800;
text-align:center;
background: linear-gradient(90deg,#00F5A0,#00D9F5,#7B61FF);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
font-size:18px;
color:#d1d5db;
margin-bottom:30px;
}

.card{
background:#1e293b;
padding:25px;
border-radius:20px;
box-shadow:0px 0px 20px rgba(0,255,255,.2);
}

.stButton>button{
width:100%;
height:50px;
border-radius:12px;
font-size:18px;
font-weight:bold;
background:linear-gradient(90deg,#7B61FF,#00D9F5);
color:white;
border:none;
}

.stButton>button:hover{
transform:scale(1.02);
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Create folder
# ----------------------------

BASE_DIR = Path("files")
BASE_DIR.mkdir(exist_ok=True)

# ----------------------------
# Header
# ----------------------------

st.markdown("<div class='big-title'>📂 FileFlow</div>", unsafe_allow_html=True)

st.markdown(
"<div class='subtitle'>Modern Python File Management System</div>",
unsafe_allow_html=True)

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("⚡ Navigation")

option = st.sidebar.radio(
    "Choose Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info("""
Built using

🐍 Python

🎈 Streamlit

📂 Pathlib
""")

# ===========================================================
# CREATE
# ===========================================================

if option == "Create File":

    st.subheader("✨ Create New File")

    filename = st.text_input("File Name")

    content = st.text_area("Content")

    if st.button("Create File"):

        path = BASE_DIR / filename

        if path.exists():
            st.error("File already exists.")

        else:
            with open(path, "w") as f:
                f.write(content)

            st.success("File created successfully 🎉")

# ===========================================================
# READ
# ===========================================================

elif option == "Read File":

    st.subheader("📖 Read File")

    filename = st.text_input("File Name")

    if st.button("Read"):

        path = BASE_DIR / filename

        if path.exists():

            with open(path) as f:
                data = f.read()

            st.code(data)

        else:

            st.error("File not found.")

# ===========================================================
# UPDATE
# ===========================================================

elif option == "Update File":

    st.subheader("🛠 Update File")

    filename = st.text_input("File Name")

    operation = st.selectbox(
        "Choose",
        [
            "Rename",
            "Append",
            "Overwrite"
        ]
    )

    path = BASE_DIR / filename

    if operation == "Rename":

        new_name = st.text_input("New Name")

        if st.button("Rename"):

            if path.exists():

                path.rename(BASE_DIR / new_name)

                st.success("Renamed Successfully")

            else:

                st.error("File not found")

    elif operation == "Append":

        text = st.text_area("Text")

        if st.button("Append"):

            if path.exists():

                with open(path, "a") as f:
                    f.write(text)

                st.success("Data Appended")

            else:

                st.error("File not found")

    elif operation == "Overwrite":

        text = st.text_area("New Content")

        if st.button("Overwrite"):

            if path.exists():

                with open(path, "w") as f:
                    f.write(text)

                st.success("File Updated")

            else:

                st.error("File not found")

# ===========================================================
# DELETE
# ===========================================================

elif option == "Delete File":

    st.subheader("🗑 Delete File")

    filename = st.text_input("File Name")

    if st.button("Delete"):

        path = BASE_DIR / filename

        if path.exists():

            path.unlink()

            st.success("Deleted Successfully")

        else:

            st.error("File not found")

# ===========================================================
# Footer
# ===========================================================

st.markdown("---")

st.caption("Made with ❤️ using Python & Streamlit")
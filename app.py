import streamlit as st
from pathlib import Path
from datetime import datetime
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="FileFlow",
    page_icon="📂",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS
# -------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
font-family:'Poppins',sans-serif;
}

.stApp{
background:
linear-gradient(
135deg,
#0f172a 0%,
#1e293b 40%,
#312e81 100%);
color:white;
}

/* Hide Streamlit */

#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

header{
visibility:hidden;
}

/* Title */

.big-title{

font-size:58px;

font-weight:800;

text-align:center;

background:
linear-gradient(
90deg,
#00F5A0,
#00D9F5,
#7B61FF,
#FF4ECD);

-webkit-background-clip:text;
-webkit-text-fill-color:transparent;

animation:glow 3s infinite alternate;

}

@keyframes glow{

from{
filter:drop-shadow(0px 0px 10px cyan);
}

to{
filter:drop-shadow(0px 0px 25px violet);
}

}

.subtitle{

text-align:center;

font-size:18px;

color:#d1d5db;

margin-bottom:25px;

}

/* Cards */

.card{

background:rgba(255,255,255,.08);

padding:25px;

border-radius:20px;

backdrop-filter:blur(15px);

border:1px solid rgba(255,255,255,.1);

box-shadow:0px 10px 30px rgba(0,0,0,.35);

margin-bottom:20px;

}

/* Sidebar */

[data-testid="stSidebar"]{

background:
linear-gradient(180deg,#111827,#1f2937);

}

[data-testid="stSidebar"] *{

color:white;

}

/* Buttons */

.stButton>button{

width:100%;

height:52px;

border-radius:14px;

font-size:17px;

font-weight:bold;

background:
linear-gradient(90deg,#7B61FF,#00D9F5);

color:white;

border:none;

transition:.3s;

box-shadow:
0px 10px 20px rgba(0,217,245,.3);

}

.stButton>button:hover{

transform:scale(1.03);

box-shadow:
0px 0px 20px cyan;

}

/* Inputs */

.stTextInput input{

background:#1f2937;

color:white;

border-radius:12px;

}

.stTextArea textarea{

background:#1f2937;

color:white;

border-radius:12px;

}

.stSelectbox{

color:black;

}

/* Code */

pre{

border-radius:15px!important;

}

/* Footer */

.footer{

text-align:center;

padding:20px;

color:#d1d5db;

font-size:14px;

}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# FILE DIRECTORY
# -------------------------------------------------

BASE_DIR = Path("files")
BASE_DIR.mkdir(exist_ok=True)

# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<div class='big-title'>
📂 FileFlow
</div>

<div class='subtitle'>
Modern File Management System using Python & Streamlit
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

files = list(BASE_DIR.iterdir())

c1,c2,c3 = st.columns(3)

with c1:
    st.metric("📂 Files", len(files))

with c2:
    st.metric("⚡ Status", "Online")

with c3:
    st.metric("🐍 Language", "Python")

st.divider()
# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.markdown("# 📂 FileFlow")

st.sidebar.markdown(
"""
Welcome 👋

Manage your files with a beautiful
Python & Streamlit interface.
"""
)

st.sidebar.markdown("---")

option = st.sidebar.radio(
    "📌 Choose an Operation",
    [
        "🏠 Dashboard",
        "✨ Create File",
        "📖 Read File",
        "🛠 Update File",
        "🗑 Delete File"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("System Status : Online 🟢")

st.sidebar.info("""
### 🛠 Tech Stack

- 🐍 Python
- 🎈 Streamlit
- 📂 Pathlib
- 💻 VS Code
""")

# -------------------------------------------------
# FILE EXPLORER
# -------------------------------------------------

st.markdown("## 📁 File Explorer")

files = sorted(BASE_DIR.iterdir())

if len(files) == 0:

    st.info("No files found. Create your first file!")

else:

    for file in files:

        size = round(file.stat().st_size / 1024, 2)

        modified = datetime.fromtimestamp(
            file.stat().st_mtime
        ).strftime("%d-%m-%Y %I:%M %p")

        with st.expander(f"📄 {file.name}"):

            col1, col2 = st.columns(2)

            with col1:
                st.write(f"**📦 Size :** {size} KB")

            with col2:
                st.write(f"**🕒 Modified :** {modified}")

            try:

                preview = file.read_text()

                if len(preview) > 300:
                    preview = preview[:300] + "..."

                st.code(preview)

            except:
                st.warning("Preview unavailable.")

st.divider()
# =====================================================
# DASHBOARD
# =====================================================

if option == "🏠 Dashboard":

    st.markdown("## 🏠 Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class='card'>
        <h3>📂 Total Files</h3>
        </div>
        """, unsafe_allow_html=True)

        st.metric("Files", len(list(BASE_DIR.iterdir())))

    with col2:

        total_size = sum(
            file.stat().st_size
            for file in BASE_DIR.iterdir()
            if file.is_file()
        )

        st.markdown("""
        <div class='card'>
        <h3>💾 Storage Used</h3>
        </div>
        """, unsafe_allow_html=True)

        st.metric(
            "Storage",
            f"{round(total_size/1024,2)} KB"
        )

    st.success("🎉 Welcome to FileFlow! Choose an operation from the sidebar.")


# =====================================================
# CREATE FILE
# =====================================================

elif option == "✨ Create File":

    st.markdown("## ✨ Create a New File")

    filename = st.text_input(
        "📄 Enter File Name",
        placeholder="example.txt"
    )

    content = st.text_area(
        "📝 File Content",
        height=250,
        placeholder="Write something amazing..."
    )

    if st.button("🚀 Create File"):

        if filename.strip() == "":
            st.warning("Please enter a file name.")

        else:

            path = BASE_DIR / filename

            if path.exists():

                st.error("❌ File already exists!")

            else:

                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)

                st.success("✅ File created successfully!")

                st.balloons()


# =====================================================
# READ FILE
# =====================================================

elif option == "📖 Read File":

    st.markdown("## 📖 Read File")

    filename = st.text_input(
        "📄 Enter File Name",
        placeholder="example.txt"
    )

    if st.button("📂 Open File"):

        if filename.strip() == "":
            st.warning("Please enter a file name.")

        else:

            path = BASE_DIR / filename

            if path.exists():

                with open(path, "r", encoding="utf-8") as f:
                    data = f.read()

                st.success("✅ File loaded successfully!")

                st.text_area(
                    "📄 File Content",
                    data,
                    height=350
                )

                size = round(path.stat().st_size/1024,2)

                modified = datetime.fromtimestamp(
                    path.stat().st_mtime
                ).strftime("%d-%m-%Y %I:%M %p")

                c1, c2 = st.columns(2)

                with c1:
                    st.metric("📦 Size", f"{size} KB")

                with c2:
                    st.metric("🕒 Modified", modified)

            else:

                st.error("❌ File not found.")
# =====================================================
# UPDATE FILE
# =====================================================

elif option == "🛠 Update File":

    st.markdown("## 🛠 Update File")

    filename = st.text_input(
        "📄 Enter File Name",
        placeholder="example.txt"
    )

    operation = st.selectbox(
        "Choose an Operation",
        [
            "✏️ Rename File",
            "➕ Append Content",
            "🔄 Overwrite Content"
        ]
    )

    path = BASE_DIR / filename

    # ----------------------------
    # Rename
    # ----------------------------

    if operation == "✏️ Rename File":

        new_name = st.text_input(
            "🆕 New File Name",
            placeholder="new_file.txt"
        )

        if st.button("✏️ Rename"):

            if filename.strip() == "" or new_name.strip() == "":

                st.warning("Please enter both file names.")

            elif not path.exists():

                st.error("❌ File not found.")

            elif (BASE_DIR / new_name).exists():

                st.error("❌ A file with this name already exists.")

            else:

                path.rename(BASE_DIR / new_name)

                st.success("✅ File renamed successfully!")

                st.balloons()

    # ----------------------------
    # Append
    # ----------------------------

    elif operation == "➕ Append Content":

        text = st.text_area(
            "Enter Content",
            height=220
        )

        if st.button("➕ Append"):

            if filename.strip() == "":

                st.warning("Please enter a file name.")

            elif not path.exists():

                st.error("❌ File not found.")

            else:

                with open(path, "a", encoding="utf-8") as f:
                    f.write("\n" + text)

                st.success("✅ Content appended successfully!")

    # ----------------------------
    # Overwrite
    # ----------------------------

    elif operation == "🔄 Overwrite Content":

        text = st.text_area(
            "New Content",
            height=250
        )

        if st.button("🔄 Overwrite"):

            if filename.strip() == "":

                st.warning("Please enter a file name.")

            elif not path.exists():

                st.error("❌ File not found.")

            else:

                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)

                st.success("✅ File updated successfully!")

                st.toast("File Saved Successfully 🎉")


# =====================================================
# DELETE FILE
# =====================================================

elif option == "🗑 Delete File":

    st.markdown("## 🗑 Delete File")

    filename = st.text_input(
        "📄 Enter File Name",
        placeholder="example.txt"
    )

    path = BASE_DIR / filename

    if filename != "":

        if path.exists():

            st.warning(
                "⚠️ This action is permanent and cannot be undone."
            )

            confirm = st.checkbox(
                "I understand. Delete this file."
            )

            if confirm:

                if st.button("🗑 Delete File"):

                    path.unlink()

                    st.success("✅ File deleted successfully!")

                    st.toast("File Deleted 🗑")

        else:

            st.error("❌ File not found.")
# =====================================================
# SEARCH FILES
# =====================================================

st.divider()

st.markdown("## 🔍 Search Files")

search = st.text_input(
    "Search by file name",
    placeholder="example.txt"
)

if search:

    results = [
        file for file in BASE_DIR.iterdir()
        if search.lower() in file.name.lower()
    ]

    if results:

        st.success(f"Found {len(results)} file(s).")

        for file in results:

            size = round(file.stat().st_size / 1024, 2)

            modified = datetime.fromtimestamp(
                file.stat().st_mtime
            ).strftime("%d-%m-%Y %I:%M %p")

            with st.expander(f"📄 {file.name}"):

                st.write(f"**📦 Size:** {size} KB")
                st.write(f"**🕒 Last Modified:** {modified}")

                try:
                    preview = file.read_text(encoding="utf-8")

                    if len(preview) > 500:
                        preview = preview[:500] + "..."

                    st.code(preview)

                except Exception:
                    st.warning("Preview unavailable.")

    else:

        st.error("No matchings are found.")


# =====================================================
# FILE STATISTICS
# =====================================================

st.divider()

st.markdown("## 📊 File Statistics")

files = list(BASE_DIR.iterdir())

total_files = len(files)

total_size = sum(
    file.stat().st_size
    for file in files
    if file.is_file()
)

largest = None

if files:

    largest = max(
        files,
        key=lambda x: x.stat().st_size
    )

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "📂 Total Files",
        total_files
    )

with c2:
    st.metric(
        "💾 Storage Used",
        f"{round(total_size/1024,2)} KB"
    )

with c3:

    if largest:

        st.metric(
            "🏆 Largest File",
            largest.name
        )

    else:

        st.metric(
            "🏆 Largest File",
            "-"
        )


# =====================================================
# RECENT FILES
# =====================================================

st.divider()

st.markdown("## 🕒 Recently Modified Files")

recent = sorted(
    files,
    key=lambda x: x.stat().st_mtime,
    reverse=True
)

if recent:

    for file in recent[:5]:

        modified = datetime.fromtimestamp(
            file.stat().st_mtime
        ).strftime("%d %b %Y %I:%M %p")

        st.write(f"📄 **{file.name}** — {modified}")

else:

    st.info("No files available.")


# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
"""
<div class="footer">

<h3>📂 FileFlow</h3>

Modern File Management System

Built with ❤️ using

🐍 Python • 🎈 Streamlit • 📂 Pathlib

<hr>

<p>
© 2026 FileFlow | Designed by <b>Payal Rawat</b>
</p>

</div>
""",
unsafe_allow_html=True
)
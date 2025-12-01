import streamlit as st
from database import Database
from models import Book

st.set_page_config(page_title = "Library App", page_icon = "📚")

db = Database()

# Create header 
st.title("📚 Library Manager")
st.write("Add books, view library and delete entries.")

# Add a book
st.subheader("➕ Add a new book.")

with st.form("add_book_form", clear_on_submit = True):
    author = st.text_input("Author")
    title = st.text_input("Title")
    submitted = st.form_submit_button("Add Book 📚")

    if submitted:
        if author.strip() == "" or title.strip() == "":
            st.error("Both author and title are required.")
        else:
            book = Book(author, title)
            db.insert_book(book.author, book.title)
            st.success(f"Added: {book}")

# List all books
st.subheader("📚 Display All Books")

show_books = st.checkbox("Show library contents")

if show_books:
    books = db.fetch_book()

    if not books:
        st.info("No books found.")
    else:
        st.write("### All Books:")

        for book_id, author, title in books:
            col1, col2, col3 = st.columns([4, 4, 1])

            with col1:
                st.write(f"**Author:** {author}")
            with col2:
                st.write(f"**Title:** {title}")
            with col3:
                delete = st.button("🗑️", key=f"delete_{book_id}")

            if delete:
                db.delete_book(book_id)
                st.experimental_rerun()

# Delete books
st.subheader("🗑️ Delete a book")

books = db.fetch_book()

if books:
    # Create a list of delete options in form "1 - Tolkien - LOTR"
    delete_options = {
        f"{book_id} - {author} - {title}": book_id
        for book_id, author, title in books
    }

    book_to_delete = st.selectbox(
        "Choose a book to delete:",
        list(delete_options.keys())
    )

    if st.button("Delete Selected Book"):
        selected_id = delete_options[book_to_delete]
        db.delete_book(selected_id)
        st.success("Book deleted.")
        st.experimental_rerun()

else:
    st.info("No books available to delete.")
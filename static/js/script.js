document.addEventListener("DOMContentLoaded", function () {
    loadPreviousBooks();
});

function fetchBook() {
    let bookId = document.getElementById("book_id").value;
    if (!bookId) {
        alert("Please enter a valid Book ID.");
        return;
    }

    fetch("/fetch_book", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `book_id=${bookId}`
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
            return;
        }
        displayBookDetails(data);
        loadPreviousBooks();
    })
    .catch(error => console.error("Error fetching book:", error));
}

function displayBookDetails(book) {
    let previewText = book.preview && book.preview.trim() !== "No preview available."
        ? marked.parse(escapeHTML(book.preview.replace(/\r\n/g, '\n')))  // Ensure line breaks render properly
        : "<p class='text-gray-400'>No preview available.</p>";

    let analysisText = book.analysis && book.analysis["Groq Analysis"] 
        ? marked.parse(escapeHTML(book.analysis["Groq Analysis"])) 
        : "<p class='text-gray-400'>No analysis available.</p>";

    document.getElementById("book_details").innerHTML = `
        <div class="bg-gray-800 p-5 rounded-md shadow-md">
            <h2 class="text-2xl font-semibold">📖 ${escapeHTML(book.Title)}</h2>
            <p><strong>✍️ Author:</strong> ${escapeHTML(book.Authors)}</p>
            <p><strong>📅 Issued:</strong> ${escapeHTML(book.Issued)}</p>
            <p><strong>📚 Subjects:</strong> ${escapeHTML(book.Subjects)}</p>

            <h3 class="mt-5 text-lg font-semibold">📜 Preview:</h3>
            <div class="bg-gray-700 p-4 rounded-md overflow-auto max-h-60 border border-gray-600 text-sm text-white">
                ${previewText}
            </div>

            <h3 class="mt-5 text-lg font-semibold">🧠 Analysis:</h3>
            <div class="bg-gray-700 p-4 rounded-md text-white border border-gray-600 text-sm">
                ${analysisText}
            </div>
        </div>
    `;
}

function loadPreviousBooks() {
    fetch("/get_books")
    .then(response => response.json())
    .then(data => {
        let bookList = document.getElementById("book_list");
        bookList.innerHTML = "";

        if (data.length === 0) {
            bookList.innerHTML = "<p class='text-gray-400'>No books accessed yet.</p>";
            return;
        }

        data.forEach(book => {
            let previewText = book.preview && book.preview.trim() !== "" 
                ? marked.parse(escapeHTML(book.preview)) 
                : "No preview available.";

            let listItem = document.createElement("li");
            listItem.className = "bg-gray-800 p-4 rounded-md shadow-md border border-gray-700";

            listItem.innerHTML = `
                <h3 class="text-lg font-semibold">📖 ${escapeHTML(book.Title)}</h3>
                <p class="text-gray-300"><strong>✍️ Author:</strong> ${escapeHTML(book.Authors)}</p>
                <p class="text-gray-300"><strong>📅 Issued:</strong> ${escapeHTML(book.Issued)}</p>

                <h4 class="mt-3 text-md font-semibold">📜 Preview:</h4>
                <div class="bg-gray-700 p-3 rounded-md text-white text-sm max-h-40 overflow-auto border border-gray-600">
                    ${previewText}
                </div>
            `;

            bookList.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error("Error loading previous books:", error);
        document.getElementById("book_list").innerHTML = "<p class='text-red-400'>Error loading books.</p>";
    });
}

// Function to escape HTML to prevent XSS attacks
function escapeHTML(str) {
    return str.replace(/[&<>"']/g, function (match) {
        const escape = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&#039;"
        };
        return escape[match];
    });
}

function toggleDarkMode() {
    document.body.classList.toggle("bg-gray-900");
    document.body.classList.toggle("text-white");
    document.body.classList.toggle("bg-white");
    document.body.classList.toggle("text-black");
}

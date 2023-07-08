import os
import requests
import tkinter as tk
import json
from tkinter import ttk
from tkinter import messagebox

# Retrieve the Custom Search Engine ID (CX) and API key from environment variables
cx = os.getenv('CX')
api_key = os.getenv('API_KEY')

def perform_search():
    # Get the query from the entry field
    query = entry.get()

    try:
        # Perform the search using the CX and API key
        response = requests.get(f"https://www.googleapis.com/customsearch/v1?cx={cx}&key={api_key}&q={query}")
        response.raise_for_status()  # Raise an exception if the response status code is not successful

        # Parse the search results
        results = json.loads(response.text)

        # Check if a result was found
        if results and 'items' in results:
            first_result = results['items'][0]

            # Display the title and URL of the first result
            title.delete(1.0, tk.END)
            title.insert(tk.END, first_result['title'])
            url.delete(1.0, tk.END)
            url.insert(tk.END, first_result['link'])
        else:
            title.delete(1.0, tk.END)
            title.insert(tk.END, "No results found")
            url.delete(1.0, tk.END)
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    except (KeyError, json.JSONDecodeError):
        messagebox.showerror("Error", "Invalid response received from the API.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

# Create the GUI window
window = tk.Tk()

# Add a title to the window
window.title("Web Search Application")

# Style the GUI window
style = ttk.Style()
style.configure('TButton', font=('calibri', 10, 'bold'), borderwidth='4')
style.configure('TEntry', font=('calibri', 12), borderwidth='4')
style.configure('TLabel', font=('calibri', 12), borderwidth='4')
style.configure('TText', font=('calibri', 12), borderwidth='4')

# Add an entry field for the search query
entry = ttk.Entry(window, width=50)
entry.pack(pady=10)

# Add a 'Search' button
button = ttk.Button(window, text="Search", command=perform_search)
button.pack(pady=10)

# Add text areas to display the title and URL
ttk.Label(window, text="Title:").pack()
title = tk.Text(window, height=2, width=50)
title.pack(pady=10)
ttk.Label(window, text="URL:").pack()
url = tk.Text(window, height=2, width=50)
url.pack(pady=10)

# Start the GUI event loop
window.mainloop()

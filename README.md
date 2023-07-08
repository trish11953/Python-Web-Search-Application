# Python Web Search Application

The Python Web Search Application is a graphical user interface (GUI) tool that allows users to perform web searches using the Google Search API. It retrieves the title and URL of the first search result and displays them in the GUI window.

## Prerequisites

- Python 3.x
- `requests` library (can be installed via `pip install requests`)
- `tkinter` library (usually included in the standard Python distribution)

## Setup

1. Clone or download the repository to your local machine.

2. Set up the required environment variables:

   - **CX**: Set the Custom Search Engine ID (CX) as an environment variable.
   - **API_KEY**: Set the API key as an environment variable.

   Make sure to replace `"your_cx_value"` and `"your_api_key_value"` with your actual CX and API key values.

   **Example for macOS/Linux**:
   
   export CX="your_cx_value"
   export API_KEY="your_api_key_value"
   
   **For Windows**: 

   set CX=your_cx_value
   set API_KEY=your_api_key_value
   

3. Open a terminal or command prompt and navigate to the directory where the `web_search_app.py` file is located.

4. Run the following command to start the application:
  ```shell
  python web_search_app.py
  ```


## Usage

1. The application window will appear.

2. Enter your search query into the entry field.

3. Click the "Search" button.

4. The title and URL of the first search result will be displayed in the respective text areas.

Please ensure that you have set the environment variables correctly and provided valid values for the Custom Search Engine ID (CX) and API key. If you encounter any issues, double-check the environment variable names and values.

> Note: The Google Custom Search JSON API has usage limits and may involve costs beyond the free quota. Review the API documentation and pricing details on the Google Cloud Platform website.
## Implementation Details

The implementation of the application follows a modular and user-friendly approach. Here are some key points on why I implemented it this way:

User Interface: The GUI is created using the tkinter library, which provides a cross-platform solution for creating interactive and visually appealing interfaces. The use of ttk widgets enhances the look and feel of the application.

Code Structure: The code is structured into separate functions, making it modular and easy to understand. The perform_search() function handles the search functionality, making an API request to retrieve search results and displaying them in the GUI.

Error Handling: Error handling is implemented to handle various exceptions that may occur during the API request and response process. It provides informative error messages to the user, helping them understand and troubleshoot any issues that may arise.

Environment Variables: The Custom Search Engine ID (CX) and API key are retrieved from environment variables. This approach allows for flexibility and security, as sensitive information can be stored securely outside of the code.

User Feedback: The application provides user feedback in the form of error messages displayed in message boxes. This ensures that the user is informed about any errors and can take appropriate actions.

By implementing the application in this way, it aims to provide a user-friendly and robust experience. The use of a GUI, modular code structure, error handling, and environment variable usage enhances usability, maintainability, and security aspects of the application.


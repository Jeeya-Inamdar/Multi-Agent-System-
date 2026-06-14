# InsightFlow: A Multi-Agent Research System

InsightFlow is a sophisticated, multi-agent system designed to automate the entire research process. It takes a user-provided topic, conducts web research, scrapes relevant content, synthesizes the information into a detailed report, and finally, provides a critical evaluation of the generated report. The entire workflow is presented through a sleek, interactive web interface built with Streamlit.

## ✨ Features

-   **Automated Research Pipeline:** A four-step process that seamlessly integrates searching, reading, writing, and critiquing.
-   **Multi-Agent Architecture:** Utilizes specialized agents for distinct tasks:
    -   **Search Agent:** Finds up-to-date and relevant sources online.
    -   **Reader Agent:** Scrapes and extracts key information from web pages.
    -   **Writer Chain:** Composes a structured and detailed research report.
    -   **Critic Chain:** Evaluates the report for quality, accuracy, and structure.
-   **Interactive UI:** A modern and responsive web application built with Streamlit, featuring custom styling for an enhanced user experience with animated and interactive elements.
-   **Source-Aware Reporting:** The final report includes a list of all source URLs used in the research, ensuring transparency and verifiability.

## 🚀 System Architecture & Workflow

The research process is orchestrated by `pipeline.py` and follows a sequential flow:

1.  **Search:** The `Search Agent`, powered by the Tavily search tool, is invoked to find recent and reliable articles on the given topic. It returns a list of titles, URLs, and snippets.
2.  **Scrape (Read):** The `Reader Agent` reviews the search results, selects the most promising URL, and uses BeautifulSoup to scrape its content. This provides a deeper context than the initial search snippets.
3.  **Write:** The `Writer Chain` receives the aggregated search results and the scraped content. It synthesizes this information into a comprehensive report, structured with an introduction, key findings, a conclusion, and a list of sources.
4.  **Critique:** The `Critic Chain` reviews the generated report, providing a score out of 10, highlighting strengths and areas for improvement, and offering a one-line verdict.

## 🛠️ Tech Stack

-   **Core Framework:** LangChain
-   **LLM Provider:** NVIDIA AI Endpoints (`moonshotai/kimi-k2.6`)
-   **Web UI:** Streamlit
-   **Tools:**
    -   **Search:** Tavily
    -   **Web Scraping:** BeautifulSoup, Requests
-   **Environment Management:** python-dotenv

## ⚙️ Setup and Installation

Follow these steps to get the project running locally.

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/jeeya-inamdar/multi-agent-system-.git
    cd multi-agent-system-
    ```

2.  **Create a Virtual Environment**
    It's recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    Create a file named `.env` in the root directory of the project and add your API keys.
    ```env
    NVIDIA_API_KEY="your_nvidia_api_key"
    TAVILY_API_KEY="your_tavily_api_key"
    ```

## Usage

There are two ways to run the research system:

### 1. Web Application (Recommended)

Launch the interactive Streamlit application.

```bash
streamlit run app.py
```

Open your browser and navigate to the local URL provided by Streamlit. Enter a research topic in the input field and click "Generate Report" to start the process.

### 2. Command-Line Interface

You can run the core pipeline directly from the command line for quick tests.

```bash
python pipeline.py
```

The script will prompt you to enter a research topic, and the entire process will run in your terminal, printing the output of each step.

## 📂 File Structure

```
└── multi-agent-system-/
    ├── agents.py           # Defines the LangChain agents (Search, Reader) and chains (Writer, Critic).
    ├── app.py              # The main Streamlit web application.
    ├── pipeline.py         # Orchestrates the end-to-end multi-agent research workflow.
    ├── requirements.txt    # Lists all Python package dependencies for the project.
    └── tools.py            # Contains the custom tools (web_search, scrape_url) for the agents.

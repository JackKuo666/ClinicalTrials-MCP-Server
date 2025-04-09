# ClinicalTrials MCP Server

[![smithery badge](https://smithery.ai/badge/@JackKuo666/clinicaltrials-mcp-server)](https://smithery.ai/server/@JackKuo666/clinicaltrials-mcp-server)

🔍 Enable AI assistants to search and access ClinicalTrials.gov data through a simple MCP interface.

The ClinicalTrials MCP Server provides a bridge between AI assistants and ClinicalTrials.gov's clinical trial repository through the Model Context Protocol (MCP). It allows AI models to search for clinical trials and access their content in a programmatic way.

🤝 Contribute • 📝 Report Bug

## ✨ Core Features
- 🔎 Trial Search: Query clinical trials with custom search strings or advanced search parameters ✅
- 🚀 Efficient Retrieval: Fast access to trial metadata ✅
- 📊 Metadata Access: Retrieve detailed metadata for specific trials using NCT ID ✅
- 📊 Research Support: Facilitate health sciences research and analysis ✅
- 📋 CSV Management: Save, load, and list CSV files with trial data ✅
- 🗃️ Local Storage: Trials are saved locally for faster access ✅
- 📊 Statistics: Get statistics about clinical trials ✅

## 🚀 Quick Start

### Installing via Smithery

To install ClinicalTrials Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/ClinicalTrials-mcp-server):

#### Claude

```bash
npx -y @smithery/cli@latest install ClinicalTrials-mcp-server --client claude --config "{}"
```

#### Cursor

Paste the following into Settings → Cursor Settings → MCP → Add new server: 
- Mac/Linux  
```s
npx -y @smithery/cli@latest run ClinicalTrials-mcp-server --client cursor --config "{}" 
```
#### Windsurf
```sh
npx -y @smithery/cli@latest install ClinicalTrials-mcp-server --client windsurf --config "{}"
```
### CLine
```sh
npx -y @smithery/cli@latest install ClinicalTrials-mcp-server --client cline --config "{}"
```


### Installing Manually
Install using uv:

```bash
uv tool install ClinicalTrials-mcp-server
```

For development:

```bash
# Clone and set up development environment
git clone https://github.com/JackKuo666/ClinicalTrials-MCP-Server.git
cd ClinicalTrials-MCP-Server

# Create and activate virtual environment
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 📊 Usage

Start the MCP server:

```bash
python clinical_trials_server.py
```

Once the server is running, you can use the provided MCP tools in your AI assistant or application. Here are some examples of how to use the tools:

### Example 1: Search for clinical trials using a search expression and save to CSV

```python
result = await mcp.use_tool("search_clinical_trials_and_save_studies_to_csv", {
    "search_expr": "COVID-19 vaccine efficacy",
    "max_studies": 5
})
print(result)
```

### Example 2: Get studies by keyword

```python
result = await mcp.use_tool("get_studies_by_keyword", {
    "keyword": "diabetes",
    "max_studies": 10
})
print(result)
```

### Example 3: Get full study details for a specific trial

```python
result = await mcp.use_tool("get_full_study_details", {
    "nct_id": "NCT04280705"
})
print(result)
```

### Example 4: Search and save studies with custom fields

```python
result = await mcp.use_tool("search_clinical_trials_and_save_studies_to_csv", {
    "search_expr": "alzheimer",
    "max_studies": 20,
    "filename": "alzheimer_studies.csv",
    "fields": ["NCT Number", "Study Title", "Brief Summary", "Conditions"]
})
print(result)
```

These examples demonstrate how to use the main tools provided by the ClinicalTrials MCP Server. Adjust the parameters as needed for your specific use case.

## 🛠 MCP Tools

The ClinicalTrials MCP Server provides the following tools:

### search_clinical_trials_and_save_studies_to_csv

Search for clinical trials using a search expression and save the results to a CSV file.

**Parameters:**
- `search_expr` (str): Search expression (e.g., "Coronavirus+COVID")
- `max_studies` (int, optional): Maximum number of studies to return (default: 10)
- `save_csv` (bool, optional): Whether to save the results as a CSV file (default: True)
- `filename` (str, optional): Name of the CSV file to save (default: corona_fields.csv)
- `fields` (list, optional): List of fields to include (default: NCT Number, Conditions, Study Title, Brief Summary)

**Returns:** String representation of the search results

### get_full_study_details

Get detailed information about a specific clinical trial.

**Parameters:**
- `nct_id` (str): The NCT ID of the clinical trial

**Returns:** String representation of the study details

### get_studies_by_keyword

Get studies related to a specific keyword.

**Parameters:**
- `keyword` (str): Keyword to search for
- `max_studies` (int, optional): Maximum number of studies to return (default: 20)
- `save_csv` (bool, optional): Whether to save the results as a CSV file (default: True)
- `filename` (str, optional): Name of the CSV file to save (default: keyword_results_{keyword}.csv)

**Returns:** String representation of the studies

### get_study_statistics

Get statistics about clinical trials.

**Parameters:**
- `condition` (str, optional): Optional condition to filter by

**Returns:** String representation of the statistics

### get_full_studies_and_save

Get full studies data and save to CSV.

**Parameters:**
- `search_expr` (str): Search expression (e.g., "Coronavirus+COVID")
- `max_studies` (int, optional): Maximum number of studies to return (default: 20)
- `filename` (str, optional): Name of the CSV file to save (default: full_studies.csv)

**Returns:** Message indicating the results were saved

### load_csv_data

Load and display data from a CSV file.

**Parameters:**
- `filename` (str): Name of the CSV file to load

**Returns:** String representation of the CSV data

### list_saved_csv_files

List all available CSV files in the current directory.

**Returns:** String representation of the available CSV files

## 🔍 MCP Resources

The ClinicalTrials MCP Server also provides the following resources:

### clinicaltrials://corona_fields

Get the corona fields data as a resource.

### clinicaltrials://full_studies

Get the full studies data as a resource.

### clinicaltrials://csv/{filename}

Get data from a specific CSV file.

**Parameters:**
- `filename` (str): Name of the CSV file

### clinicaltrials://available_files

Get a list of all available CSV files.

### clinicaltrials://study/{nct_id}

Get a specific study by NCT ID.

**Parameters:**
- `nct_id` (str): The NCT ID of the clinical trial

### clinicaltrials://condition/{condition}

Get studies related to a specific condition.

**Parameters:**
- `condition` (str): The condition to search for

## Usage with Claude Desktop

Add this configuration to your `claude_desktop_config.json`:

(Mac OS)

```json
{
  "mcpServers": {
    "ClinicalTrials": {
      "command": "python",
      "args": ["-m", "ClinicalTrials-mcp-server"]
      }
  }
}
```

(Windows version):

```json
{
  "mcpServers": {
    "ClinicalTrials": {
      "command": "C:\\Users\\YOUR_USERNAME\\AppData\\Local\\Programs\\Python\\Python311\\python.exe",
      "args": [
        "-m",
        "ClinicalTrials-mcp-server"
      ]
    }
  }
}
```
Using with Cline
```json
{
  "mcpServers": {
    "ClinicalTrials": {
      "command": "bash",
      "args": [
        "-c",
        "source /home/YOUR/PATH/ClinicalTrials-MCP-Server/.venv/bin/activate && python /home/YOUR/PATH/ClinicalTrials-MCP-Server/clinical_trials_server.py"
      ],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

After restarting Claude Desktop, the following capabilities will be available:

### Searching Clinical Trials

You can ask Claude to search for clinical trials using queries like:
```
Can you search for recent clinical trials about diabetes?
```

The search will return basic information about matching trials including:

• Trial title

• NCT Number

• Conditions

• Brief Summary


### Getting Trial Details

Once you have an NCT ID, you can ask for more details:
```
Can you show me the details for trial NCT04280705?
```

This will return:

• Full trial title

• Conditions

• Brief Summary

• Other available details


## 📁 Project Structure

- `clinical_trials_server.py`: The main MCP server implementation using FastMCP
- `clinical_trials.py`: Contains helper functions for interacting with the ClinicalTrials.gov API

## 🔧 Dependencies

- Python 3.10+
- FastMCP
- pytrials
- pandas

You can install the required dependencies using:

```bash
pip install FastMCP pytrials pandas
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## ⚠️ Disclaimer

This tool is for research purposes only. Please respect ClinicalTrials.gov's terms of service and use this tool responsibly.

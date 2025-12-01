# LLM-Based Product Match Verification

This project uses an LLM to check whether a customer search query correctly matches a product. It loads two ESCI dataset files, formats the product information into a prompt, and returns a structured output indicating whether the match is correct and how the query should be corrected if not.

---

## Required Data

Download the following two files from the Amazon ESCI dataset:

- `shopping_queries_dataset.parquet`
- `product_catalogue.parquet`

Place both files in the folder referenced by your `DATA_PATH` environment variable.

---

## Setup

This project was developed using Python 3.11.14.

Install dependencies:

```bash
pip install -r requirements.txt
```

Create an .env file:

```bash
OPENAI_API_KEY=your_key
DATA_PATH=/path/to/esci/files
```

## Project Structure

```src/
src/
    data_loading/
        data_loader.py
    llm/
        client.py
        prompt.py
        label_verifier.py
        llm_output_model.py
    settings/
        config.py
project_walkthrough.ipynb
README.MD
requirements.txt
```

- data_loading: loads, merges, and filters the ESCI datasets
- llm: prompt template, API wrapper, schema, and verifier
- project_walkthrough.ipynb: short end-to-end demonstration of the pipeline

## Running the Demo:

Open and run:

```bash
project_walkthrough.ipynb
```

The notebook loads the two ESCI files, selects a small sample, constructs the prompt, calls the LLM, and displays the final match results.
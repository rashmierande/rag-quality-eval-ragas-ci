#Automated RAG Quality Testing with RAGAS + GitHub Actions
[[!RAGAS Tests](https://github.com/rashmierande/rag-quality-eval-ragas-ci/actions/workflowes/ragas-tests.yml/badge.svg)](https://github.com/rashmierande/rag-quality-eval-ragas-ci/actions/workflows/ragas-tests.yml)

Automatically test RAG answer quality on every pull request using RAGAs metrics and GitHub Actions.
Demo for the RAGAS tests showing PR

## What this does:
This project demonstrates how to:
1. Automatically evaluate RAG system quality using RAGAs metrics
2. Run tests on every pull request via GitHub Actions
3. Enforce quality thresholds before merging code
4. Display results directly in PR comments

# Metrics Evaluated
Metrics                    What It Measures                                               Threshold
Faithfulness               Answer uses only retrieved context (no hallucinations)         >=0.7
Relevancy                  Answer addresses the question asked                            >=0.7
Context Precision          Retrived documents are relevant to the question                >=0.7
Context Recall             All necessary context was retrieved                            >=0.7

# How to get Started
## 1. Clone the repo
``` bash
git clone https://github.com/rashmierande/rag-quality-eval-ragas-ci.git
cd rag-quality-eval-ragas-ci
```
## 2. Install Dependencies
``` bash
pip install -r requirements.txt
```
## 3. Setup OpenAI API Key

Add your OpenAI API key to GitHub repo secrets:
- Go to settings -> Secrets and variables -> Actions
- Add new secret: `OPENAI_API_KEY`

## 4. Run tests locally
``` bash
export OPENAI_API_KEY="your key here"
python tests/ragas_test.py
```
## 5. Create a Pull Request
Tests run automatically on every PR. Results appear as a comment:
``` markdown
## RAGAs Test Results
Metric              Score           Threshold       Status
Faithfulness        0.78            0.7             Pass
Relevancy           0.85            0.7             Pass
Context Precision   0.79            0.7             Pass
Context Recall      0.82            0.7             Pass

***All tests passed! Safe to merge.
```
## Project Structure
```
ragas-github-actions-demo/
├── .github/
│   └── workflows/
│       └── ragas-tests.yml       # GitHub Actions workflow
├── tests/
│   ├── ragas_test.py             # Test execution script
│   └── test_data.json            # Test dataset (Q&A pairs)
├── prompts/
│   └── api_assistant.py          # Example prompt template
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Test Data Format
Test Data in 'tests/test_data.json' follows this structure:
``` json
{
    "question": "How do I authenticate with the API?",
    "answer": "Authentication requires an API Key...",
    "contexts":[
        "API authentication uses Bearer token...",
        "Format:Authorization:Bearer YOUR_API_KEY"
    ],
    "ground_truth":"Use Bearer token in Authorization header..."
}
```
## Customization
## Adjust Quality Thresholds
Edit 'tests/ragas_test.py`:
```python
thresholds = {
    'faithfulness':0.8, #Increase for stricter checks
    'relevancy':0.7,
    'context_precision':0.7,
    'context_recall':0.7
}

# Add more tests
Add entries to 'tests/test_data.json' with your own Q&A pairs.
##Use different LLM
Replace OpenAI with AWS Bedrock, Azure OpenAI, or other provider by modifying RAGAs config.

## Example workflow
1. Developer updates prompt template in `prompts/api_assistant.py`
2. Creates pull request with changes
3. GitHub Actions triggers automatically
4. RAGAS evaluates answer quality against test dataset
5. Results posted to PR as comment
6. Build passes/fails based on thresholds
7. Developer fixes issues if tests fail
8. Merge when all tests pass

##Learn More
- [RAGAS Documentation](https://docs.ragas.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Blog Post: Why RAG Quality Testing Matters](#) *(coming soon)*

## Contributing
Contributions welcome! Feel free to:
- Add more test cases
- Improve the workflow
- Add support for other LLM providers
- Enhance the PR comment formatting

##License

##Questions?
Open an issue or reach out on  https://www.linkedin.com/in/rashmierande/

**⭐ If this helped you, please star the repo!**


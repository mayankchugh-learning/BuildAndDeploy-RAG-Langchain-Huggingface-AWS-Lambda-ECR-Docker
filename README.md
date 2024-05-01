# BuildAndDeploy-RAG-Langchain-Huggingface-AWS-Lambda-ECR-Docker
# Deploying RAG APPLICATION using AWS(AWS lambda,AWS ECR), Langchain, Huggingface using Docker and infrastructure setuo on AWS(AWS lambda,AWS ECR)


## Git commands

```bash
git add .

git commit -m "Updated"

git push origin main
```
### STEPS:
## How to run? 
### STEP 01- Create a conda environment after opening the repository
```bash
conda create -p llmopsapr24_env python -y
```

```bash
source activate ./llmopsapr24_env
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```

```bash
python app.py
```
# P6 (8% of grade): Learning about LLMs

Github Classroom Link: https://classroom.github.com/a/et18YGBr

## :telescope: Overview

This project introduces you to working with Large Language Models (LLMs) using the HuggingFace API, fine-tuning them on specific data, and visualizing results using Streamlit. Additionally, you will explore Retrieval-Augmented Generation (RAG) and its advantages over fine-tuning, integrating it into a full ETL pipeline.

Learning Objectives:

- Gain hands-on experience with pre-trained LLMs, including text generation, prompt engineering, and 4-bit quantization.
- Fine-tune LLMs using LoRA on domain-specific datasets, tracking and evaluating performance improvements.
- Build and deploy interactive apps with Streamlit.
- Implement a RAG pipeline using Elasticsearch with Haystack to enhance LLM response accuracy.
- Compare Fine-Tuning vs RAG to determine which is better suited for an exam preparation tool based on lecture transcripts.

Before starting, please review the [general project directions](../projects.md).

:warning: Please use Piazza to post (public/private) any questions regarding this project, as e-mails will NOT be answered. If you need to include your code to get help, please make a **private** post.

## :pushpin: Corrections/Clarifications

- 4/25: Added a note about `wandb` for Q2.2.
- 4/30: Added submission clarifications and details for setting up Elasticsearch.
- 5/2:  Added a note allowing `q3.pdf` instead of screenshots.

## :hammer_and_wrench: Section 0: Setup

### Step 1: Google Colab or Kaggle

This project requires you to submit **two notebook files**. **Both Section 1 and Section 2 require the use of a GPU**. **Google Colab** and **Kaggle** both provide free access to GPUs (e.g., **NVIDIA Tesla T4**). However, GPU resources on **Google Colab** are **not guaranteed**, as they depend on availability. Feel free to use **Google Colab** if you can secure resources; otherwise, please use **Kaggle**. 

The **third Section** of the project requires running **Elasticsearch** locally.


#### For Google Colab:
1. Sign-in to [Google Colab](https://colab.research.google.com) with your "wisc.edu" ID.
2. Create a new notebook and name it `p6.ipynb`.
3. To enable GPU:
    * In the upper-right of the Colab window, select ▾ (**Additional connection options**).
    * Select **Change runtime type**.
    * Under **Hardware accelerator**, select **T4 GPU**.
4. While you have free access to GPUs, there are usage limits you should be aware of:
    * Sessions may last up to 12 hours, but inactive sessions will be terminated sooner.
    * Resources (e.g., GPU availability) are **not** guaranteed and depend on demand.
    * When you are not actively working, disconnect and exit from your session so don't get slowed down later.

#### For Kaggle:
1. Sign-in to [Kaggle]( https://www.kaggle.com/) with your "wisc.edu" ID.
2. On the tab-bar, select on **Code**, and create a new notebook and name it `p6.ipynb`.
3. To enable GPU: **Settings → Accelerator → GPU P100**
4. While you have free access to GPUs, there are usage limits you should be aware of:
    * You have maximum 30 hours/week of GPU access.

**Code to Verify GPU Availability**
```python
import torch
print("GPU available:", torch.cuda.is_available())
print("GPU name:", torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU")
```
### Step 2: Setup a HuggingFace Account

You'll be accessing models via HuggingFace's `transformers` library, which requires setting up an account.

**Steps to Set Up**:
1. [HuggingFace](https://huggingface.co) and sign up for a free account.
2. After logging in, navigate to your profile and obtain an API token:
    * Go to your account settings → **Access Tokens**.
    * Click **New Token** and generate a token with the role "read".
3. Store the token securely; you’ll need it for authentication.

**Login in Colab/Kaggle**:
1. Authenticate your HuggingFace account in Colab or Kaggle by running the following code:
```python
from huggingface_hub import login
login()
```
This will prompt you to enter your HuggingFace API token.

### Step 3: Apply for `Llama-3.2-1B-Instruct` Acccess on HuggingFace.
1. Go to https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct. Fill-out and submit the provided form to gain access to the model weights.
    * You can review your request status (pending/accepted) here: https://huggingface.co/settings/gated-repos. It typically takes ~15 minutes.

**If your access request is denied**: Use any of the other fine-tuned variants of the same model family (preferably instruction-tuned). For e.g., one variant is an uncensored version, [`huihui-ai/Llama-3.2-1B-Instruct-abliterated`](https://huggingface.co/huihui-ai/Llama-3.2-1B-Instruct-abliterated).

### Step 4: Install Dependencies

1. Please install the required dependencies by running the following code:
```python
!pip install bitsandbytes>=0.39.0
!pip install --upgrade accelerate transformers datasets peft trl
!pip install streamlit
!npm install -g localtunnel
```

### Step 5: Download Dataset

1. The dataset of lecture transcripts (1.txt, 2.txt, etc.) is provided as a ZIP file. Download and extract the files into your Colab or Kaggle environment using `wget` and `unzip`.

```
!wget https://github.com/CS639-Data-Management-for-Data-Science/s25/raw/main/p6/transcripts.zip
!unzip transcripts.zip -d transcripts/
```

## :blue_book: Section 1: Text Generation with a Pre-Trained LLM

In this section, you will load and run inference (text generation) on a **4-bit quantized version** of [Llama-3.2-1B-Instruct](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/), using HuggingFace [`transformers`](https://huggingface.co/docs/transformers/en/index) and [`bitsandbytes`](https://huggingface.co/docs/transformers/main/en/quantization/bitsandbytes).

### Q1.1: Load a 4-bit quantized `Llama-3.2-1B-Instruct` model and and its tokenizer.

**Steps to follow**:
1. Import the required classes: `AutoTokenizer`, `AutoModelForCausalLM`, and `BitsAndBytesConfig`.
2. Set the model ID to `"meta-llama/Llama-3.2-1B-Instruct"`.
3. Define a configuration for 4-bit quantization using `BitsAndBytesConfig` with the following settings:
    * `load_in_4bit=True`
    * `bnb_4bit_quant_type="nf4"`
    * `bnb_4bit_compute_dtype=torch.float16`
4. Load the tokenizer using `AutoTokenizer.from_pretrained()`.
5. Load the quantized model using `AutoModelForCausalLM.from_pretrained()` with the quantization configuration, and ensure it is moved to the current device (e.g., GPU).
6. If your access request for `Llama-3.2-1B-Instruct` was denied and you used a different model, please include a markdown cell including the name and link to the model.

<details>
<summary>[<b>Optional reading</b>] How do we access pre-trained models from HuggingFace?</summary>

- HuggingFace `transfomers` provides several ways to load pre-trained models depending on the specific task you want to accomplish:
    - `pipeline()`:
        - Quickest way to load a pre-trained model *and* tokenizer for popular tasks like text generation, summarization, etc. It is the most user-friendly, but less customizable than other methods.
    - General [`AutoClasses`](https://huggingface.co/docs/transformers/en/model_doc/auto):
        - `AutoModel.from_pretrained()` and `AutoTokenizer.from_pretrained()` guess and automatically retrieve the relevant model given the name/path to the pretrained weights/vocabulary.
    - Task-Specific [`AutoClasses`](https://huggingface.co/docs/transformers/en/model_doc/auto):
        - `AutoModelForCausalLM`, `AutoModelForSequenceClassification`, etc. perform similarly as `AutoModel`, but retrive task-optimized models (for e.g., `AutoModelForCausalLM` will attach an additional head for casual language modeling).
    - Specific Models and Tokenizers:
        - HuggingFace also provides model and tokenizer classes tied to specific architectures/vocabularies. For e.g, [`LlamaModel.from_pretrained()`](https://huggingface.co/docs/transformers/main/en/model_doc/llama#transformers.LlamaModel), [`LlamaForCausalLM.from_pretrained()`](https://huggingface.co/docs/transformers/main/en/model_doc/llama#transformers.LlamaForCausalLM), [`LlamaTokenizer.from_pretrained()`](https://huggingface.co/docs/transformers/main/en/model_doc/llama#transformers.LlamaTokenizer), etc.
</details>

### Q1.2: Test your quantized model with different prompts (text generation).

Test your quantized `Llama-3.2-1B-Instruct` model by generating text responses to 2-3 different prompts. Ensure at least **one prompt** is related to **UW-Madison**.

**Steps to follow**:
1. Use the tokenizer's `.encode()` method to tokenize the model input (your prompt).
    * Refer to the [`.encode()` documentation](https://huggingface.co/docs/transformers/en/main_classes/tokenizer#transformers.PreTrainedTokenizer.encode). However, we need more than just the input IDs for the tokens in order to get the model to generate output. So, we'll be using `tokenizer` as a callable function, which will enable us to obtain: input IDs, attention mask in relevant torch tensor format. You can use the `help(tokenizer.__call__)` function to read through the relevant documentation.
2. Use the model's `.generate()` method to generate output.
    * Refer to the [`.generate()` documentation](https://huggingface.co/docs/transformers/en/main_classes/text_generation#transformers.GenerationConfig).
    * Feel free to play with the generation settings (e.g., `max_new_tokens=100`)
3. Use the tokenizer's `.decode()` method to convert model output into human-readable text.
    * Refer to the [`.decode()` documentation](https://huggingface.co/docs/transformers/en/main_classes/tokenizer#transformers.PreTrainedTokenizer.decode).
    * Set `skip_special_tokens=True` to remove special tokens from the output.
4. For each prompt, print both the **input prompt** and the **generated output text**.


### Q1.3: Identify a prompt where the model fails and analyze the failure.

- Find a prompt that your quantized `Llama-3.2-1B-Instruct` model fails to answer correctly.
    * Print both the **input prompt** and the **generated output text**.
-  In a markdown cell, write **1-2 reasons** why the model failed for the chosen prompt. Consider factors such as:
    * Lack of relevant training data.
    * Limitations in multi-step reasoning or contextual understanding.

### Q1.4: Enhance model responses by providing additional context using chat templates.

Explore how to improve your model's responses by providing additional context using the [chat templates](https://huggingface.co/docs/transformers/main/en/chat_templating) to create a role-playing agent.

**Steps to follow**:
1. Use your tokenizer's `.apply_chat_template()` method to structure a role-playing prompt. For example (please try to come up with your **own** prompt):
    * Role as a teacher: "You are a knowledgeable science teacher explaining string theory to a 10-year-old."
    * Role as a poet: "You are a skilled poet writing a haiku about quantum computing."
    * Role as a pirate: "You are a pirate who uses 'blistering barnacles' in their conversations frequently, and are currently answering questions about sailing."
2. Pass the resulting formatted prompt to your model using `.generate()`.
3. Decode and print the output as done previously.
4. In a markdown cell, note whether the role-playing prompt got the model to successfully respond in the assumed role/character.

## :green_book: Section 2: Fine-Tuning a Pre-Trained LLM on Course Lecture Transcripts

In this section, you will fine-tune your quantized `Llama-3.2-1B-Instruct` model on the lecture transcripts of this course. The goal is to specialize the model to provide more accurate and context-specific answers related to the course material.

### Q2.1: Test the model before fine-tuning.

**Steps to Follow**:
1. Pick **any** course-specific prompt. For e.g., "Can you summarize the main topics and associated tools used?", "What NoSQL databases are covered in the course?", etc.
2. Use your tokenizer's `.apply_chat_template()` method to assign a specific role to your model:
    ```
    "You are an instructor of CS 639 Data Management for Data Science course at UW-Madison, and are currently answering student questions."
    ```
3. Print both the **input prompt** and the **generated output text**.


### Q2.2 Fine-tune the model on course lecture transcripts with LoRA.

**Steps to follow**:
1. Import the required classes:
    ```python
    from datasets import Dataset

    from peft import LoraConfig
    from transformers import TrainingArguments
    from trl import SFTTrainer
    ```
2. Load and process the dataset.
    * Split the dataset in train and test splits (e.g. 90% train and 10% test).
    * Convert the splits into a HuggingFace `Dataset` object.
3. Tokenize the train and test splits using your tokenizer.
4. Fine-tune the model using `SFTTrainer`. Ensure that both **training loss** and **validation loss** are printed for each epoch.
    * Use the following LoRA configurations (feel free to modify them if you'd like):
        ```python
        lora_config = LoraConfig(
            r=8,
            task_type="CAUSAL_LM",
            target_modules=[
                "q_proj", "o_proj", "k_proj", "v_proj",
                "gate_proj", "up_proj", "down_proj"
            ],
        )
        ```
    * Use the following training arguments (feel free to modify them if you'd like, except `num_train_epochs`):
        ```python
        training_args = TrainingArguments(
            eval_strategy="epoch",
            save_strategy="epoch",
            num_train_epochs=10,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            gradient_accumulation_steps=4,
            learning_rate=2e-4,
            fp16=True,
            logging_steps=1,
            logging_dir="./logs",
            output_dir="./results",
            save_total_limit=2,
            optim="paged_adamw_8bit"
        )
        ```
    [Note] The program will prompt you to supply a [Weights & Biases](https://wandb.ai/home) (`wandb`) API key to track metrics such as loss during your training run. `wandb` is an incredibly useful tool for analyzing your training runs, so make an account and play around with the graphs it gives you!
    * It is **OK if some of the epochs are auto-skipped by `SFTTrainer`** during fine-tuning. This is related to `gradient_accumulation_steps=4` setting.

### Q2.3: Test the model after fine-tuning.

- Evaluate your fine-tuned model’s performance on the same prompt used in `Q2.1`
    * Print both the **input prompt** and the **generated output text**. 
- In a mark-down cell, note if there is any improvmenents in quality, relevance, or accuracy of response.

## :orange_book: Section 3: Building an Exam Preparation Chatbot using RAG

In this section, you will create an interactive Streamlit application that functions as an **Exam Preparation Chatbot**. This chatbot will leverage **Retrieval-Augmented Generation (RAG)** to dynamically retrieve relevant lecture materials from Elasticsearch before generating responses using a pre-trained LLM.

Unlike fine-tuned models that have static knowledge, RAG provides real-time, contextual answers by pulling up-to-date course content. This makes it ideal for helping students prepare for exams by ensuring that their responses are accurate, relevant, and grounded in course materials.

**Your goal is to:**
- Build an interactive Streamlit app that retrieves and generates answers based on lecture transcripts, using Elasticsearch with Haystack.
- Host models using Huggingface API (this allows you to do this part of the project without GPUs).
- Display the top 3 retrieved documents to provide transparency on where the information is coming from.
- Compare RAG vs Fine-Tuning by testing which approach produces better exam-related answers.
- Be creative! You can enhance your chatbot by adding summarization, filtering, or other features.

![ETL + RAG Pipeline](assets/p6_flow_chart.png)

---

### :hammer_and_wrench: Setting Up Elasticsearch

This section requires you to run **Elasticsearch** locally.

Refer to the [P3's guidelines](https://github.com/CS639-Data-Management-for-Data-Science/s25/tree/main/p3#hammer_and_wrench-setting-up-elasticsearch-using-docker) to set up Elasticsearch with Docker and configure Jupyter and the Python Elasticsearch Client.  
Please create a new notebook in Jupyter and name it `p6_part3.ipynb`.
 
### Q3.1: Load Class Transcripts into Elasticsearch

To build an end-to-end pipeline, you must load your lecture transcripts into Elasticsearch [look here for more info](https://haystack.deepset.ai/integrations/elasticsearch-document-store):

```python
from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore

document_store = ElasticsearchDocumentStore(hosts="http://localhost:9200", basic_auth=(username, password), index=index_name)
```

You may alternatively use [Elastic Cloud](https://www.elastic.co/cloud) to host the server, in which case your snippet will look something like this:
```python
from haystack_integrations.document_stores.elasticsearch import ElasticsearchDocumentStore

document_store = ElasticsearchDocumentStore(hosts="<url Elastic Cloud provides>", api_key="<Deployment API key>", index=index_name)
```

### Q3.2: Implement the Streamlit App

![streamlit_example](assets/streamlit_example.png)

**You will need these**
- [Haystack Huggingface tutorial](https://docs.haystack.deepset.ai/docs/huggingfaceapigenerator)
- For the model, you must use `microsoft/Phi-3.5-mini-instruct` and its accompanying template:
    - ```python
        template = """
        <|system|>
        You are a helpful assistant.<|end|>
        <|user|>
        Given the following information, answer the question.

        Context: 
        {% for document in documents %}
            {{ document.content }}
        {% endfor %}

        Question: {{ query }}?<|end|>
        <|assistant|>"""
        ```
- For the Streamlit integration, roughly follow [this guide](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)
    - Use the following snippet for compatibility with our `microsoft/Phi-3.5-mini-instruct`:
        - ```python
            st.title("💬 Course Chatbot")
            st.caption("🚀 Interactive Q&A with Elasticsearch, Haystack, and HuggingFace")

            if "messages" not in st.session_state:
                st.session_state.messages = []

            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

            if prompt := st.chat_input("Ask a question about the course transcripts"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                st.chat_message("user").write(prompt)

                response = rag_pipeline.run({
                    "prompt_builder": {"query": prompt},
                    "retriever": {"query": prompt}
                })['llm']['replies'][0]

                st.session_state.messages.append({"role": "assistant", "content": response})
                st.chat_message("assistant").write(response)
            ```
- Take a screenshot of your Streamlit interface as `q3.png` (or make a pdf as `q3.pdf`).

**Tips**:
- Before you begin this section, reset all variables and clear memory using:
    ```python
    %reset -f
    ```
- Since Streamlit apps cannot run natively in Google Colab or Kaggle, you'll have to follow some steps to deploy and access your app:
    1. **Save your app code**: Use the `%%writefile` magic command to save all the app code into a file named `app.py`. Include the following line at the top of the code cell containing your app:
    ```python
    %%writefile app.py
    ```
    2. **Generate a LocalTunnel password**: Run the following command to generate and a LocalTunnel password, and copy it.
    ```shell
    !curl https://loca.lt/mytunnelpassword
    ```
    3. **Launch the app**: Deploy your app by running the following command, which launches Streamlit on port `8501` and exposes it via LocalTunnel:
    ```shell
    !streamlit run app.py & npx localtunnel --port 8501
    ```
    - Once executed, this command will provide a public URL, such as: `https://<random_name>.loca.lt`. Use this link to access your app in a web browser, and use the password from Step 2.

### Q3.3: Compare Fine-Tuning vs RAG

Test the same set of prompts on both your fine-tuned LLM and RAG pipeline.

**Report:**

- Which approach gave more accurate responses?
- Did the fine-tuned model hallucinate information?
- Was RAG better at answering new/unseen questions?

Some helpful resources:
- [Streamlit cheat sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)

## :outbox_tray: Submission

- If you used **Google Colab** for the first two parts of the project, you are required to submit a **PDF** file of the notebook (`p6.pdf`). Otherwise, submit the **ipynb** file (`p6.ipynb`).
- Additionally, submit your solution for part 3 as `p6_part3.ipynb`.
- `q3.png` is your screenshot of Streamlit from Q3 (or `q3.pdf`).

- The structure of the required files for your submissions is as follows:
```
p6-<your_team_name>
|--- README.md (list names and e-mail IDs of team members at the top)
|--- p6.pdf (or p6.ipynb if you didn't use Google Colab)
|--- p6_part3.ipynb
|--- q3.png
```
- **If you have more than 1 member in your team**: please include a markdown cell, titled "Contributions", at the *beginning* or *end* of `p6.ipynb` that lists the contributions of each team member. For e.g.:  
```markdown
# Contributions
Jane: Q1.1-1.4, Q2.1-2.3
John: Q3
```

- **Technical issues within 36 hours of the deadline will not be considered as an excuse for late submission.**

### Point breakdown

Breakdown of total 12 points is as follows:
- Section 1: 3.5 points
   * Q1.1: 0.5 point 
   * Q1.2-Q1.4: 1 point each
- Section 2: 4 points
   * Q2.1: 0.5 points
   * Q2.2: 3 points
   * Q2.3: 0.5 points
- Section 3 (Q3): 4.5 points

## :trophy: Testing

Submissions will be **manually** graded.

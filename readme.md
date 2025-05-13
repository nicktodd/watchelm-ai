# Building and Deploying a GenAI Solution
This exercise is designed to help demystify the world of Generative AI for technologists by
giving you a step by step guide to building and deploying a GenerativeAI application from scratch - all on a single computer running nothing but Docker.


The pre-requisites for this exercise are that you have access to a machine with Docker installed, and that also has a 'decent' GPU. I haven't tested what 'decent' means, but I have had it working on 3 different machines - a Surface book, a desktop computer, and an AWS EC2 GPU instance.


## Step 1 Launch the Relevant Docker containers

1. Log in to your environment and ensure that docker is installed. To verify Docker is there, run the following command:

```
docker --version
```

2. You will firstly run the anythingllm container. AnythingLLM  https://anythingllm.com/ is a tool that according to the Web site:

*Everything great about AI in one desktop application. Chat with docs, use AI Agents, and more - full locally and offline.*

We will be using it as a Web front end to allow us to query and interact with our LLM. It will also host a Vector store for us and allow us to create and then configure our Embeddings.

The command you need to run is:

```
docker run -d -p 3001:3001 mintplexlabs/anythingllm:1.8.1
```

** Warning:** Note the version number was needed when 1.8.2 was not working. 13/5/25


3. You will now run a second container hosting the LLM. We will use Ollama. 


Ollama is a lightweight, open-source framework that allows you to run large language models (LLMs) locally on your computer with minimal setup. 

You can run this and specify to use your GPUs using the following Docker command:

```
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

4. Before you proceed, verify that both of your containers are working without any problems. You can do this using:

```
docker ps
```

You should see two separate containers running. If you do not, ask your instructor for assistance. If you are doing this remotely, you can view the logs from the container that exited using:

```
docker log YOUR_CONTAINER_ID
```

5. Once you have verified that your containers are both running, you can now install LLMs into the Ollama container.

3. Use exec to log into the ollama container and run the following command:


```
docker exec –it CONTAINER_ID /bin/bash


ollama pull phi3:mini
ollama pull all-minilm
```

The ```ollama pull``` command is used to pull LLMs into your container. You can see the available LLMs here: https://ollama.com/search


4. Finally, to verify that everything is set up correctly, visit your Docker container running anythingllm here:

http://IP_OF_MACHINE:3001


## Complete the Initial Set up of AnythingLLM

To use AnythingLLM we have to do some basic set up. This involves setting our default LLM and whether we want a password for access and a few other things. The instructions are below:

1. Once the Web page loads, click the **Get Started** button.

2. From the list of LLM providers, select **Ollama**. It will automatically detect your docker container running Ollama and you will get a green message notifying you.

3. At the **Ollama model** selector, choose **phi3:mini**. Leave the max tokens as is for now.

4. Now click the right arrow button, and for the users, select **Just me**. For the password, select **No**.

5. Click the right arrow again. It shows the summary of your current options. Click the right arrow once more and then click **Skip Survey**.

6. For the Workspace name, enter your name and then the word Workspace. eg. ```FredWorkspace```. Click the right arrow one last time and it will save your new workspace.

## Turn Off Web Access

We don't want our queries to involve the Internet, so we will turn this off for Anything LLM.

1. Using the spanner in the bottom left, navigate to **Settings**. Then select **Agent Skills**. Deselect the option for **Web Scraping** and **Web Search**.

2. Now click the **Back** icon button at the bottom left of the screen.


## Set up Embedding Configuration

AnythingLLM can help us with creating our embeddings. You will do configure this now.

1. Move the mouse to hover over your Workspace and then click the **Settings** icon.

2. In the settings you can set the various parameters, specifically the Chat settings, which are the parameters that are used for the chat. Review the options. We don't need to do anything here just yet, but notice you can set the temperature for example.

3. Now using the bottom left spanner, we can enter the settings for AnythingLLM.
 
4. Expand all the collapsed menu items to see what is available. 

5. Under **AI providers**, select **Embedder**. Set the embbedder to **Ollama** (not all the available models are embedding models). Remember, embedding allows us to set up the RAG data for our model.

6. Select the **all-minilm** model.

7.  Leave the chunk left as the default value for now.

The chunking will be important to chunk courses based on the XML tags or each file.

Note that the AnythingLLM UI has only basic options for chunking. The actual LLM does have more sophisticated options (such as at XML tags for example). 

^To sort the chunk sizes you can edit /app/server/utils/TextSplitter/index.js and then find the class called the RecursiveSplitter. In the class, modify the constructor to have a separators default argument which is a string array of splitters, so in my case, it could be separators such as: ['</course>', '\n\n', '\n', ' ']. You might also remove all the other XML tags in some other function.^

8. Click **Save changes**.

9. Now on the left menu, select **Text Splitter and Chunking**. The chunk size cannot be larger than the splitter size. You can leave the default values for now. In a real application, you would be experimenting with different values here - a bit like the chunking.

10. Use the bottom left back arrow to go back to the workspace.

## Set up Some Embeddings

1. To embed, hover over the Workspace and then click the **Upload** icon (which is actually for embedding).

2. Select the files you want to embed. For the exercise, these are a set of course files which you can download from here:

https://training.watchelm.com/xml_originals.zip

You will need to download and extract the zip locally, and then upload the folders to AnythingLLM - it doesn't like the zip file directly!


3. Collapse the file list and then select the radio button next to the full set and click **Move to workspace** and then click **Save and embed**.

## Test the Application

You have now set up Ollama with a model, and you have set up some embeddings.

You can now test the AI to see if you can ask questions about the training courses that you have provided as embeddings.

1. Click on your Workspace in the left pane.

2. Ask a question. Something like, "Can you recommend me a course on Java?"

3. How good is the response?


You can now try different configurations to see if you can improve the quality of your response.

A good response will refer to the courses you uploaded, a bad response might simply suggest you use Udemy!




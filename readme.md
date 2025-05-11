Run the docker image using the nvidia card

1. docker run -d -p 3001:3001 mintplexlabs/anythingllm

2. docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama



Visit http://localhost:3001

Note: grok is a chatgpt that uses the web and scrapes the web

1. Do the initial setup of the UI and select the model that you want to use.

2. You will need to go into the Agent settings and deselect the option for Web scraping.

2. For the workspace on the left, choose settings

3. In the settings you can set the various parameters, specifically the Chat settings, which are the parameters that are used for the chat.

4. Now using the bottom left spanner, we can enter the settings for AnythingLLM.

5. Expand all the collapsed menu items and set the following:

6. Set the embbedder to Ollama (not all the available models are embedding models). embedding allows us to set up the RAG data for our model.

7. In my example, select the all-minilm model.

8.  Set the chunk length based on the content being embedded and how you want to use it. Note that the text splitter will actually be the main determiner of the chunk length.
  

Note that the chunking happens at the front end. It will be important to chunk courses based on the XML tags or each file.
The UI does not have any options to enable this, but the CLI does actually support it through lots of additional chunking options.
To sort the chunk sizes you can edit /app/server/utils/TextSplitter/index.js and then find the class called the RecursiveSplitter. In the class, modify the constructor to have a separators default argument which is a string array of splitters, so in my case, it could be separators such as: ['</course>', '\n\n', '\n', ' ']. You might also remove all the other XML tags in some other function.




10. Save changes.

11. Now go to text splitter and chunking. The chunk size cannot be larger than the splitter size. In my examples I set the overlap to be 32.

12. Use the bottom left back arrow to go back to the workspace.

13. To embed, hover over the Workspace and click the Upload button (which is actually for embedding).

14. Select the files you want to embed.

15. Collapse the file list and then select the radio button next to the full set and click Move to workspace and then click Save and embed.

16. Now visit your workspace and ask it about one of your embedded files.



Use /reset to reset the thread.







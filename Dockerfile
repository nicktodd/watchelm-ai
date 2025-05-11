FROM ollama/ollama
# small model for fast inference
RUN ollama pull phi4-mini
RUN ollama pull gemma3:12b-it-qat
# for other models, visit https://ollama.com/library


# used for reasoning (shows it's reasoning as well as doing the inference)
# this did not work well for course outlines as it kept referring to courses elsewhere
# RUN ollama pull phi4-mini-reasoning


# used for embedding
# RUN ollama pull all-minilm 
RUN ollama pull nomic-embed-text
# Alternative embedding models if needed
# RUN ollama pull mxbai-embed-large

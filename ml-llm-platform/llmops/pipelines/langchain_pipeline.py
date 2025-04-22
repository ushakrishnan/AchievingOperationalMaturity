from langchain import LLMChain, PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import SequentialChain

# Define the prompt templates
prompt_template_1 = PromptTemplate(
    input_variables=["input_text"],
    template="Given the following input: {input_text}, what are the key insights?"
)

prompt_template_2 = PromptTemplate(
    input_variables=["insights"],
    template="Based on these insights: {insights}, generate a summary."
)

# Initialize the language model
llm = OpenAI(model_name="gpt-3.5-turbo")

# Create the individual chains
chain_1 = LLMChain(llm=llm, prompt=prompt_template_1)
chain_2 = LLMChain(llm=llm, prompt=prompt_template_2)

# Create a sequential chain
pipeline = SequentialChain(chains=[chain_1, chain_2], input_variables=["input_text"], output_variables=["summary"])

def run_pipeline(input_text):
    """Run the LangChain pipeline with the provided input text."""
    result = pipeline.run(input_text=input_text)
    return result

if __name__ == "__main__":
    # Example usage
    input_text = "The advancements in AI technology have led to significant changes in various industries."
    summary = run_pipeline(input_text)
    print("Generated Summary:", summary)
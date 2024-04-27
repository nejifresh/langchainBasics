from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv(), override=False)

from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain



def main():
    print("Welcome to LangChain")
    llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
    response = llm.invoke('What is your name?')
    print(response)



def prompt_template_basics():
    print("Welcome to learning prompt templates basics")
    #STEP 1: DEFINE A TEMPLATE
    template = "Tell me a {joke_type} joke about {subject} "

    #STEP 2: Create the prompt template
    my_joke_template = PromptTemplate.from_template(template)

    #STEP 3: Create a prompt and Inject the variable in the prompt template just created
    joke_prompt = my_joke_template.format(subject="rocks", joke_type="funny")

    #Step 4: We now create chain (Components: PROMPT TEMPLATE, LLM)
    llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
    # joke_chain = LLMChain(prompt=joke_prompt, llm=llm)
    # result = joke_chain.run()
    result = llm.predict(text=joke_prompt)
    print(result)

def prompt_template_advanced():
    #Advacned prompt templates
    from langchain_core.prompts import ChatPromptTemplate
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant called {name} you specialize in {job}"),
            ("human", "Hello how are you doing?"),
            ("ai", "I am doing very ok thanks"),
            ("human", "{user_input}")
    ]
    )

    messages = chat_template.format_messages(name="Johnson", job="carpentry", user_input="How do i fix a broken door?")
    llm = ChatOpenAI(openai_api_key=os.getenv('OPENAI_API_KEY'))
    result = llm.invoke(input=messages)
    print(result.content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    prompt_template_advanced()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

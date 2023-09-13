from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from dotenv import load_dotenv

load_dotenv()
llm =  OpenAI(temperature=0.0)

def generate_restaurant_name_and_iteams(cuisine):
    # Generate restaurant name
    prompt_temp_name1=PromptTemplate(
        input_variables=["cuisine"],
        template="i want to open an restaurant for {cuisine} food. suggest me name for restaurant"
    )

    name_chain = LLMChain(llm=llm , prompt=prompt_temp_name1,output_key="restaurant_name")

    # generate menu Iteams
    prompt_temp_iteams = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""suggest some menu iteams for {restaurant_name} , and return with comma seperated values"""
    )

    food_item_chain = LLMChain(llm=llm,prompt=prompt_temp_iteams,output_key="menu_items")  

    chain = SequentialChain(
        chains=[name_chain,food_item_chain],
        input_variables=["cuisine"],
        output_variables = ["restaurant_name","menu_items"])
    
    response = chain({"cuisine":cuisine})

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_iteams("Indian"))

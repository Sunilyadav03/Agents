from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import re
import httpx

load_dotenv()

llm= ChatOpenAI(model= "gpt-4o")


class Chatbot:
    def __init__(self,system=""):
        self.system=system
        self.message=[]
        if self.system:
            self.message.append({"role":"system","content":system})
    def __call__(self,message):
        self.message.append({"role":"user","content":message})
        result=self.execute()
        self.message.append({"role":"assistant","content":result})
        return result
        
    def execute(self):
        llm= ChatOpenAI(model= "gpt-4o")
        result = llm.invoke(self.message)
        return result.content
        

prompt = """
You run in a loop of Thought, Action, PAUSE, Observation.
At the end of the loop your output an Answer.
Use Thought to describe your thoughts about the question you have been asked.
Use Action to run one of the actions available to you - then return PAUSE.
Observation will be the result of running those actions.


Your available actions are:
calculate:
e.g. calculate: 4 * 7 / 3
Runs a calculation and returns the number - uses Python so be sure to use floating point
syntax if necessary

wikipedia:
e.g. wikipedia: Django
Returns a summary from searching Wikipedia

simon_blog_search:
e.g. simon_blog_search: Python
Search Simon's blog for that term

Example session:
Question: What is the capital of France?
Thought: I should look up France on Wikipedia
Action: wikipedia: France
PAUSE

You will be called again with this:
Observation: France is a country. The capital is Paris.

You then output:
Answer: The capital of France is Paris

Please Note: if you get basic conversation questions like "hi","hello","how are you?",\n
you have to answer "hi","hello","i am good".
""".strip()

action_re = re.compile('^Action: (\w+): (.*)')

def wikipedia(query):
    response = httpx.get("https://en.wikipedia.org/w/api.php", params={
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json"
    })
    return response.json()["query"]["search"][0]["snippet"]

def simon_blog_search(query):
    response = httpx.get("https://datasette.simonwillison.net/simonwillisonblog.json", params={
        "sql": """
        select
          blog_entry.title || ': ' || substr(html_strip_tags(blog_entry.body), 0, 1000) as text,
          blog_entry.created
        from
          blog_entry join blog_entry_fts on blog_entry.rowid = blog_entry_fts.rowid
        where
          blog_entry_fts match escape_fts(:q)
        order by
          blog_entry_fts.rank
        limit
          1
        """.strip(),
        "_shape": "array",
        "q": query,
    })
    return response.json()[0]["text"]

def calculate(number):
    return eval(number)

known_actions = {
    "wikipedia": wikipedia,
    "calculate": calculate,
    "simon_blog_search": simon_blog_search
}


def query(question,max_turns=5):
    i = 0
    bot = Chatbot(prompt)
    next_prompt = question
    while i < max_turns:
        i += 1
        result = bot(next_prompt)
        print(result)
        actions = [action_re.match(a) for a in result.split('\n') if action_re.match(a)]
        if actions:
            action, action_input = actions[0].groups()
            if action not in known_actions:
                raise Exception(f"Unknown action: {action}: {action_input}")
            print(" -- running {} {}".format(action, action_input))
            observation = known_actions[action](action_input)
            print("Observation:", observation)
            next_prompt = f"Observation: {observation}"
        else:
            return result
        
query("Has Simon written about LLMs?")
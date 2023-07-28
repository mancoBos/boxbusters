import pandas as pd
from scipy import spatial  # for calculating vector similarities for search
import openai
import tiktoken
import pickle

openai.api_key ='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'
GPT_MODEL = 'gpt-4-32k'
EMBEDDING_MODEL = "text-embedding-ada-002"  # OpenAI's best embeddings as of Apr 2023

with open('data/uploads/correspondence_embeds.pk', 'rb') as handle:
    correspondence_df = pickle.load(handle)
with open('data/uploads/heatwave_embeds.pk', 'rb') as handle:
    heatwave_df = pickle.load(handle)

heatwave_df = heatwave_df["heatwave_df"]
correspondence_df = correspondence_df["correspondence_df"]
concat_df = pd.concat([correspondence_df, heatwave_df], ignore_index=True)
example_df = concat_df.iloc[5:]


def strings_ranked_by_relatedness(
    query: str,
    df: pd.DataFrame,
    relatedness_fn=lambda x, y: 1 - spatial.distance.cosine(x, y),
    top_n: int = 100
) -> tuple[list[str], list[float]]:
    """Returns a list of strings and relatednesses, sorted from most related to least."""
    query_embedding_response = openai.Embedding.create(
        model=EMBEDDING_MODEL,
        input=query,
    )
    query_embedding = query_embedding_response["data"][0]["embedding"]
    strings_and_relatednesses = [
        (row["text"], relatedness_fn(query_embedding, row["embedding"]))
        for i, row in df.iterrows()
    ]
    strings_and_relatednesses.sort(key=lambda x: x[1], reverse=True)
    strings, relatednesses = zip(*strings_and_relatednesses)
    return strings[:top_n], relatednesses[:top_n]

# examples
# strings, relatednesses = strings_ranked_by_relatedness("increasingly high temperatures", concat_df, top_n=5)
# for string, relatedness in zip(strings, relatednesses):
#     print(f"{relatedness=:.3f}")
#     display(string)


def num_tokens(text: str, model: str = GPT_MODEL) -> int:
        """Return the number of tokens in a string."""
        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text))


def query_message(
            query: str,
            df: pd.DataFrame,
            model: str,
            token_budget: int
    ) -> str:
        """Return a message for GPT, with relevant source texts pulled from a dataframe."""
        strings, relatednesses = strings_ranked_by_relatedness(query, df)
        introduction = 'See the below articles for relevant context. If the answer cannot be found in the articles, write "I could not find an answer."'
        question = f"\n\nQuestion: {query}"
        message = introduction
        for string in strings:
            next_article = f'\n\nMessage introduction:\n"""\n{string}\n"""'
            if (
                    num_tokens(message + next_article + question, model=model)
                    > token_budget
            ):
                break
            else:
                message += next_article
        return message + question


def ask(
            query: str,
            df: pd.DataFrame = concat_df,
            model: str = GPT_MODEL,
            token_budget: int = 8000,
            print_message: bool = False,
    ) -> str:
        """Answers a query using GPT and a dataframe of relevant texts and embeddings."""
        message = query_message(query, df, model=model, token_budget=token_budget)
        if print_message:
            print(message)
        messages = [
            {"role": "system", "content": "You answer questions about the 2022 Winter Olympics."},
            {"role": "user", "content": message},
        ]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0
        )
        response_message = response["choices"][0]["message"]["content"]
        return response_message


example = open('data/uploads/example_embed.txt','r')
example = example.read()


test_file = ask("Please summarise the message in less than 200 words"+ example)

# additional_context = ask("Can you provide additional useful context from previous policies and heatwave news about the example in less than 100 words"+example)
additional_context = ask('Tell me about the current heatwaves in Europe in less than 80 words.')

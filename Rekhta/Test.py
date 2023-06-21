import requests

api_endpoint="https://api.openai.com/v1/completions"

api_key="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"

request_header={
    "Content-Type":"application/json",
    "Authorization":"Bearer "+api_key
}

query="extract only the name of singer from this paragraph without any fullstop"
query+=""" Din Kuchh Aise Guzaarta Hai Koi | Gulzar Nazm In His Own Voice Recitation : Din Kuchh Aise Guzaarta Hai Koi Written & Recited by Gulzar

Nazm is a form of Urdu poetry that is often used to write about one singular subject in a regular or free rhyme scheme as per the demand of the subject and wish of the poet. Unlike the Ghazal, which comprises of several self contained and independent couplets, expressing various thoughts and feelings in the same metre or rhyme scheme, the Nazm is not bound by any such compulsion. The flee-verse poem called "Azad Nazm" is a modern variation, having the freedom to use lines without rhyme of unequal length in the same poem, or even in the same stanza. The poet thus empowers his words to sound more intense and bring them as close as possible to the intonation and rhythms of natural speech. However, an inner rhythm with an understanding of the obligatory metre keeps it within the ambit of poetry, which brings about a charming musicality to this form of Urdu verse.

Mood : Sadness
Theme :- Philosophical
Genre : Sufi

Label :: Saregama India Ltd

For more videos log on & subscribe to our channel :"""


request_data={
    "model":"text-davinci-003",
    "prompt":query,
    "max_tokens":1000,
    "temperature":0
}

response=requests.post(api_endpoint,headers=request_header,json=request_data)

if response.status_code==200:
    response = response.json()
    output_generated = response["choices"][0]
    print(output_generated["text"].strip("\n"))
else:
    print("Error Occured with status code:",response.status_code)
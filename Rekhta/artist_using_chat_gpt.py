import requests

def get_artist_name(title, description):
    api_endpoint="https://api.openai.com/v1/completions"

    # api_key="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"
    api_key = "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"

    request_header={
        "Content-Type":"application/json",
        "Authorization":"Bearer "+api_key

    }

    query=f"extract only the name of singer from this paragraph without any fullstop \n{title} \n{description}"

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
        return output_generated["text"].strip("\n")
    else:
        return "Error Occured with status code:" + str(response.status_code)
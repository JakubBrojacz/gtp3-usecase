# https://github.com/Shubhamsaboo/kairos_gpt3/blob/master/GPT-3_Sandbox/email_generation/model_training_service.py

import openai


class Code:
    def __init__(self):
        print("Model Intilization--->")
        with open('training_data.txt', 'r') as f:
            self.training_data = f.read()
        print(self.training_data)

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "engine": "davinci",
            "temperature": 0.85,
            "max_tokens": 100,
            "best_of": 2,
            "stop": ["Input:"]
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.Completion.create(prompt=prompt, **kwargs)["choices"][0]["text"].strip()
        return r

    def model_prediction(self, input, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        openai.api_key = api_key
        output = self.query(self.training_data.format(input))
        return output

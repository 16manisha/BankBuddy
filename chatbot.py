import openai
from plaid import Client

openai.api_key = "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"

def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    while True:
        user_input = input("Ask your banking question: ")
        if user_input.lower() == "exit":
            break
        print("AI Response:", chatbot_response(user_input))



plaid_client = Client(client_id="67adf2740245ff0021df5562", 
                      secret="e1aa0a1d748787ebb944c952abd17e", 
                      environment="sandbox")

def get_bank_balance():
    accounts = plaid_client.Accounts.get(access_token="your_access_token")
    return accounts["accounts"][0]["balances"]["available"]

if __name__ == "__main__":
    balance = get_bank_balance()
    print("Your bank balance:", balance)

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

def generate_text(prompt_text, max_length=50, temperature=0.8):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    prompt_text = "You: " + prompt_text + "\nAI:"
    inputs = tokenizer.encode(prompt_text, return_tensors="pt", truncation=True, max_length=1024)
    attention_mask = torch.ones_like(inputs)

    outputs = model.generate(
        inputs, 
        attention_mask=attention_mask, 
        max_length=max_length, 
        num_return_sequences=1,
        temperature=temperature,
        pad_token_id=tokenizer.eos_token_id
    )
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    generated_text = generated_text.split("AI:")[1].strip()

    return generated_text

def main():
    print("Terminal GPT-2 - Weirdo Edition (Real)")
    print("Made by @immayr on youtube. Subscribe now or face the consequences.")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        generated_text = generate_text(user_input, max_length=100, temperature=0.7)
        print("AI: ", generated_text)

if __name__ == "__main__":
    main()

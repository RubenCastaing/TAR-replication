# Use a pipeline as a high-level helper
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Correct model name
model_name = "distilgpt2"

# Initialize pipeline
pipe = pipeline("text-generation", model=model_name)

# Load model directly
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare input
inputs = tokenizer("Hello, my dog is cute", return_tensors="pt")

# Forward pass with labels to compute loss
outputs = model(**inputs, labels=inputs["input_ids"])

# Extract loss and logits
loss = outputs.loss
logits = outputs.logits

print(f"Loss: {loss.item()}")
print(f"Logits Shape: {logits.shape}")

output_sequences = model.generate(**inputs, max_length=50, num_return_sequences=1)

# Decode and print generated text
generated_text = tokenizer.decode(output_sequences[0], skip_special_tokens=True)
print(f"Generated text: {generated_text}")

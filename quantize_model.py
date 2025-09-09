from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Path to the pre-trained Nexa model
model_path = "models/omni-vlm"  # Adjust if your folder differs

# Quantization config (8-bit using bitsandbytes)
print("Loading model in 8-bit...")
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    load_in_8bit=True,
    device_map="auto"  # use GPU if available
)

tokenizer = AutoTokenizer.from_pretrained(model_path)

# Save quantized model to a new folder
quantized_path = "models/omni-vlm-8bit"
model.save_pretrained(quantized_path)
tokenizer.save_pretrained(quantized_path)

print(f"Quantized model saved to: {quantized_path}")

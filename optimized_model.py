import torch
from transformers import AutoModelForCausalLM
from nexa_sdk import image_to_text, OmniVLM

# 1. Load the model using Nexa SDK
print("🔄 Loading OmniVLM...")
model = OmniVLM(model_path="NexaAI/OmniVLM-968M")  # Hugging Face model

# 2. Get the actual PyTorch model object
torch_model = model.model  # This may vary depending on Nexa SDK version

# 3. Quantize to 4-bit precision
print("⚡ Quantizing to 4-bit...")
quantized_model = AutoModelForCausalLM.from_pretrained(
    "NexaAI/OmniVLM-968M",
    load_in_4bit=True,
    device_map="auto"
)

# 4. Save quantized model
quantized_model.save_pretrained("OmniVLM_4bit")
print("✅ Quantized model saved at OmniVLM_4bit/")

# 5. Export to ONNX for edge devices
print("📦 Exporting to ONNX...")
dummy_input = torch.randint(0, 1000, (1, 128))  # Example fake input
torch.onnx.export(
    quantized_model,
    dummy_input,
    "OmniVLM_4bit.onnx",
    opset_version=17,
    input_names=["input_ids"],
    output_names=["logits"]
)
print("✅ Exported model as OmniVLM_4bit.onnx")

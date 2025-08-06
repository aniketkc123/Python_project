from nexa_sdk import image_to_text

image_path = "C:\Users\anike\OneDrive\Desktop\vlm_images\WhatsApp Image 2025-07-11 at 19.47.32_82854dea.jpg"

print("🔄 Running OmniVLM on:", image_path)
result = image_to_text(image_path)
print("✅ Result:", result)

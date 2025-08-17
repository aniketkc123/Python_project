# NeuroDrishti Internship – Detailed Overview

## Introduction
During my internship at **NeuroDrishti Pvt Ltd (IIT Kanpur incubated startup)**, I worked on developing and optimizing AI pipelines for **smart glasses for visually impaired users**. The focus was on reducing cloud dependency by exploring **on-device deployment of Vision-Language Models (VLMs) and Large Language Models (LLMs)**, with an emphasis on quantization, pruning, and lightweight integration.

------------------------------------------------------------
## Goals of the Internship
1. Explore the feasibility of deploying lightweight LLMs/VLMs on smart glasses hardware.
2. Investigate model optimization techniques such as **quantization, pruning, and knowledge distillation**.
3. Design end-to-end **technical pipelines** for smart glasses (camera input to audio output).
4. Test integration approaches: **on-device only, hybrid (device + cloud), split model execution**.

------------------------------------------------------------
## Work Done

### 1. Model Exploration
- Looked into Nexa AI SDK VLM and open-source models.
- Tried to run Nexa VLM locally using PyCharm and llama.cpp.
- Found that models were accurate but too heavy for direct on-device deployment.

### 2. Environment Setup
- Used PyCharm for development and build testing.
- Tried compiling llama.cpp with cmake to support quantized GGUF models.
- Faced dependency and build issues initially.

### 3. Quantization
- Applied **Post-Training Quantization (PTQ)** using bitsandbytes, llama.cpp, and GGUF formats.
- Experimented with **INT8 and INT4 quantization**.
- Outcome: Model size reduced by ~70% but vision-text alignment accuracy degraded.

### 4. Pruning & Distillation
- Explored pruning redundant neurons and layers in CNN/Vision Transformers.
- Looked into distillation from large VLMs to smaller student models.
- Did not complete full implementation, but identified it as a viable future direction.

### 5. Smart Glasses Pipeline Design
- Designed detailed end-to-end technical pipelines:
  - **On-Device**: Entire inference on device (lightweight models).
  - **Hybrid**: On-device + cloud for heavy tasks.
  - **Split Execution**: Encoder on-device, decoder on cloud.
- Defined modules: Object Detection, OCR, VLM/LLM, TTS, ASR.

------------------------------------------------------------
## Learnings
- **Direct quantization** of large VLMs caused significant accuracy drop.
- Hybrid model execution (device + cloud) is more practical for real-time applications.
- Task-specific **distilled models** can make glasses more efficient for accessibility.
- Integration of models on ARM/embedded hardware requires optimized runtimes (TensorRT, OpenVINO, RKNN).

------------------------------------------------------------
## Outcomes
1. A working knowledge base of **model optimization techniques** for embedded deployment.
2. Documented **pipelines for smart glasses**, covering multiple technical approaches.
3. Identified **bottlenecks in quantization** and proposed future improvements.
4. Gained practical experience in **AI model deployment workflows** (PyCharm, llama.cpp, GGUF, Nexa SDK).

------------------------------------------------------------
## Future Recommendations
- Apply **QLoRA (Quantization + LoRA)** for efficient fine-tuning of small VLMs.
- Build a **domain-specific dataset** for navigation, object detection, and text reading tasks.
- Train a **specialized student VLM** with reduced vocabulary tailored for accessibility use cases.
- Explore **dedicated hardware accelerators** for real-time performance (NPU/TPU/RK3588).

------------------------------------------------------------
## Conclusion
The internship provided me with hands-on exposure to **practical challenges of running AI models on constrained hardware**. While full on-device deployment of large VLMs is not yet feasible, I successfully explored multiple optimization approaches, created detailed pipelines, and identified a clear roadmap for future development of **assistive smart glasses** at NeuroDrishti.


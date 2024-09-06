from diffusers import DiffusionPipeline
import torch

pipeline = DiffusionPipeline.from_pretrained("./model_weights/photopediaXL_45/", torch_dtype=torch.float16).to("cuda")
pipeline.load_textual_inversion("./model_weights/testing_textual_inversion_lamon", weight_name="learned_embeds.safetensors")

if __name__ == '__main__':
    image = pipeline("A <lamon-toy> besides a mountain", num_inference_steps=50).images[0]
    image.save("fake-lamon.png")


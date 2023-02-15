from happytransformer import HappyGeneration, GENSettings
import time

def load_model() -> HappyGeneration:
    #TODO: load_path가 안 되는 원인 조사하기
    model = HappyGeneration(model_type= "GPT-NEO", model_name="Pheol/nietzsche")
    return model

def generate(prompt: str) -> str:
    model: HappyGeneration = load_model()
    settings = GENSettings(min_length= 20, max_length= 70, do_sample=True, top_k=0, temperature=0.7)
    result: str = model.generate_text(prompt, args = settings).text
    return result
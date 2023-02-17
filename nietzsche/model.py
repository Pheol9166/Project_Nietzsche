from happytransformer import HappyGeneration, GENSettings
import time

def load_model() -> HappyGeneration:
    #TODO: load_path가 안 되는 원인 조사하기
    model = HappyGeneration(model_type= "GPT-NEO", model_name="Pheol/nietzsche")
    return model

def generate(prompt: str, set_vals: tuple[int, float]) -> str:
    model: HappyGeneration = load_model()
    length, top_P = set_vals
    settings = GENSettings(min_length= 20, max_length= length, do_sample=True, top_p= top_P)
    result: str = model.generate_text(prompt, args = settings).text
    return result
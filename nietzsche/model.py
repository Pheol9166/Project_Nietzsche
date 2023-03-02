from happytransformer import HappyGeneration, GENSettings


# git LFS의 용량 제한으로 인해 모델을 로컬에서 불러오지 않는 방식으로 만들었습니다.
def load_model() -> HappyGeneration:
    model = HappyGeneration(model_type= "GPT-NEO", model_name="Pheol/nietzsche")
    return model

def generate(prompt: str, set_vals: tuple[int, int, float]) -> str:
    model: HappyGeneration = load_model()
    length, top_K, top_P = set_vals
    settings = GENSettings(min_length= 20, max_length= length, do_sample=True, top_k= top_K, top_p= top_P)
    result: str = model.generate_text(prompt, args = settings).text
    return result
from happytransformer import HappyGeneration, GENSettings
import pickle


def load_model() -> HappyGeneration:
    """_파인튜닝된 모델을 불러오는 함수입니다._

    pickle 파일로 로컬 내에서 불러오는 방식과 huggingface에서 모델을 불러오는 방식 비교
    pickle 파일 사용 시: 1초 내외
    huggingface로 불러올 시: 5초 내외
    
    Returns:
        HappyGeneration: _파인튜닝된 모델입니다._
    """
    # model = HappyGeneration(model_type= "GPT-NEO", model_name="Pheol/nietzsche")
    with open("./DB/models/nietzsche.pkl", "rb") as f:
        model: HappyGeneration = pickle.load(f)
 
    return model

def generate(prompt: str, set_vals: tuple[int, int, float]) -> str:
    """_파인튜닝된 모델을 기반으로 답변을 생성하는 함수입니다._

    Args:
        prompt (str): _사용자의 문장입니다._
        set_vals (tuple[int, int, float]): _문장의 최대 길이, top_k, top_p의 값입니다._

    Returns:
        str: _생성된 문장입니다._
    """
    model: HappyGeneration = load_model()
    length, top_K, top_P = set_vals
    settings = GENSettings(min_length= 20, max_length= length, do_sample=True, top_k= top_K, top_p= top_P)
    result: str = model.generate_text(prompt, args = settings).text

    return result

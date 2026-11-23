from segment import segment
from fastapi import FastAPI

app = FastAPI()

@app.get("/segment")
def get_segment(text: str):
    segmented = segment(text)
    output_list = []
    for item in segmented:
        output_list.append(item["word"])

    return {"segmented": output_list}
    

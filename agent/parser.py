import json

def parse_response(text):
    try:
        return json.loads(text)
    except:
        return {"type": "final", "content": text}

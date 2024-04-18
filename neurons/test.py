import requests

class MyClass:
    def __init__(self, text):
        url = "https://www.scribbr.com/ai-detector.php"
        headers = {
            "Referer": "https://www.scribbr.com/ai-detector/",
            "Origin": "https://www.scribbr.com",
        }
        data = {
            "text": text,
            "lang": "en"
        }
        response = requests.post(url, headers=headers, json=data)
        print(response.json()['data']['text_score'])

# Example usage
my_instance = MyClass('text')
# result = my_instance.get_new_prediction("This is a test text")
# print(result)
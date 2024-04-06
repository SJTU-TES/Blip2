from utils.models import get_processor_and_model,lora_fit
from utils.get_input import get_input
device_map = {'language_model':"cuda",\
	'language_projection':'cpu', \
	'qformer':'cpu', \
	'query_tokens':'cpu', \
	'vision_model':'cpu'}
modelpath="pretrained"
# modelpath="Salesforce/blip2-opt-2.7b"

processor,model=get_processor_and_model(modelpath=modelpath,device_map=device_map)

lora_fit(model)

url = "https://ts1.cn.mm.bing.net/th/id/R-C.75eb2f4b2ba18ad45bef900cb84f1afa?rik=0ypFQ%2fHNlRZomQ&riu=http%3a%2f%2fyouimg1.c-ctrip.com%2ftarget%2ftg%2f551%2f901%2f988%2fb6c0b42fab064d0ba93e6d8160b8a799.jpg&ehk=1vNUtkCQznGRxCgjJrxgSZtOO7xgpxHCQviI9GNSuiQ%3d&risl=&pid=ImgRaw&r=0"
question = "Question: what is the main elements in the picture? Answer:"
inputs = get_input(processor=processor,url=url,text=question,local_img=False)
out = model.generate(**inputs, max_length=200)
answer=processor.decode(out[0], skip_special_tokens=True).strip()
print(question)
print(answer)
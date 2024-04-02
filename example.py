from utils.models import get_processor_and_model,lora_fit
from utils.get_input import get_input
device_map = {'language_model':"cuda",\
	'language_projection':'cpu', \
	'qformer':'cpu', \
	'query_tokens':'cpu', \
	'vision_model':'cpu'}
modelpath="img2text"
# modelpath="Salesforce/blip2-opt-2.7b"

processor,model=get_processor_and_model(modelpath=modelpath,device_map=device_map)

lora_fit(model)

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# url = ".\.jpg"
question = "Question: is there water in the picture?? Answer:"
inputs = get_input(processor=processor,url=url,text=question,local_img=False)
out = model.generate(**inputs, max_length=200)
answer=processor.decode(out[0], skip_special_tokens=True).strip()
print(question)
print(answer)
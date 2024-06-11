from typing import Dict,Any
from app.openai_client import openai_client

class AiImage:
    def __init__(self,prompt: Dict[str,Any]):
        self.look_and_feel = prompt['look_and_feel']
        self.business_type = prompt['business_type']
        self.text = prompt['text']
        self.colors = prompt['colors']

    def imageGenerator(self):

        data =[]
        if self.text:
            data.append(f'The icon should prominently feature the company name {self.text}')
        if self.look_and_feel:
            data.append(f'With a {self.look_and_feel} look and feel')
        if self.colors and len(self.colors) > 0 :
            colors = ','.join(self.colors)
            data.append(f'The design should revolve around a color theme composed of {len(self.colors)} colors specifically, {colors}')
        if self.business_type:
            data.append(f'The use of colors should be balanced to enhance the icon"s aesthetic appeal while maintaining the {self.business_type} essence of the business')


        final_prompt = f"Generate an icon {'.'.join(data)}"

        # data = f"Generate an icon with a ${prompt['look_and_feel']} look and feel, who has a ${prompt['business_type']} type of business. Icon will contain a   "
        
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=final_prompt,
            size="256x256",
            quality="standard",
            n=1,
        )

        print(final_prompt,response)
        image_url = response.data[0].url
        return image_url

import gradio as gr
from transformers import pipeline
import re



text_summarizer_pipeline = pipeline('summarization')



def greetMe(articleInput, min_length_of_article, max_length_of_article):

    articleToBeSummarized = articleInput

    if len(re.findall(r'\w+', articleToBeSummarized)) < 250:

        return "The length of the total article should be of minimum 250 words."

    elif len(re.findall(r'\w+', articleToBeSummarized)) > 750:

        return "THe length of the total article should be not greater than 750 words."
    
    else:

        summarizedArticle = text_summarizer_pipeline(articleToBeSummarized, min_length=min_length_of_article, max_length=max_length_of_article, do_sample=False)

        return summarizedArticle[0]['summary_text']



myapp = gr.Interface(fn=greetMe, 
                     title="Text Summarizer using Transformers",
                     inputs=[
                         gr.Textbox(lines=20, placeholder="enter the original text that is to be summarized", label="Text Input Field", interactive=True),
                         gr.Slider(10, 30, value=10, step=10, label="Minimum number of words in Summarized Article", info="Choose between 10 and 30"),
                         gr.Slider(120, 150, value=120, step=10, label="Maximum number of words in Summarized Article", info="Choose between 120 and 150"),
                     ],
                     outputs=gr.Textbox(lines=20, label="Summarized Text Output", show_copy_button=True),
                     allow_flagging='never')


if __name__=="__main__":
    myapp.launch(show_api=False)

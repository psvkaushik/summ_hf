from transformers import pipeline
import gradio as gr

model = pipeline('summarization')
def predict(prompt):
    output = model(prompt)[0]['summary_text']
    return output

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter the text to summarize", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs='text')

demo.launch()

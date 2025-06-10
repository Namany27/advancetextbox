
import gradio as gr
from gradio_advancetextbox import AdvanceTextbox


example = AdvanceTextbox().example_value()

demo = gr.Interface(
    lambda x:x,
    AdvanceTextbox(label="📦 AI-Generated Course Plan", lines=18, interactive=False, show_copy_button=True, show_download_button=True),  # interactive version of your component
    AdvanceTextbox(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()

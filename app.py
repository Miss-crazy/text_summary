from flask import Flask , render_template , request
from transformers import pipeline 
import math 

app = Flask(__name__)

#load summarization pipeline
summarizer = pipeline("summarization" , model="facebook/bart-large-cnn")

#split larhe input paragram into smaller manageable chunks based on a fixed number of words
def chunk_text(text , max_chunk_len=1000):
    words = text.split()
    chunks=[]
    for i in range(0 , len(words), max_chunk_len):
        chunk = " ".join(words[i:i +max_chunk_len])
        chunks.append(chunk)
    return chunks 

#Summarizes each chunk separately by feeding it to the Hugging Face summarization pipeline.
def summarize_large_text(text):
    chunks = chunk_text(text)
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk , max_length = 300 , min_length = 40 , do_sample= False)
        summaries.append(summary[0]['summary_text'])
    combined_summary = " ".join(summaries)
    #If the combined summary is still very long, it summarizes this combined summary again to shorten it further.
    if len(combined_summary.split()) >1000:
        combined_summary = summarizer(combined_summary , max_length = 300 , min_length=40,do_sample=False)[0]['summary_text']
    return combined_summary

@app.route('/')

def home():
    return render_template('index.html')

@app.route('/summarize',methods=['POST'])

def summarize_route():
    input_text = request.form['inputtext']
    final_summary = summarize_large_text(input_text)
    return render_template('output.html' , summary = final_summary)

if __name__ == '__main__':
    app.run(debug=False)
    
    
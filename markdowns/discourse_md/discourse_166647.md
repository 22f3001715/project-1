- # id
  
  592777
  
  # username
  
  23f1001806
  
  # name
  
  Dhruv Gupta
  
  # post_url
  
  /t/i-have-doubt-in-q10/166647/1
  
  # created_at
  
  2025-02-09T14:51:52.566Z
  
  # cooked
  
  <p>I have doubt in question 10 to convert pdf to markdown<br>
  I am not getting correct markdown<br>
  <a class="mention" href="/u/pds_staff">@pds_staff</a></p>
  
  # topic_id
  
  166647
  
  # topic_title
  
  I have doubt in Q10
- # id
  
  593235
  
  # username
  
  22f3000092
  
  # name
  
  Ashutosh Banerjee 
  
  # post_url
  
  /t/i-have-doubt-in-q10/166647/2
  
  # created_at
  
  2025-02-09T18:15:12.582Z
  
  # cooked
  
  <p>Try using the pymupdf4llm Library<br>
  pip install pymupdf4llm</p>
  <p>import pymupdf4llm<br>
  md_text = pymupdf4llm.to_markdown(“input.pdf”)</p>
  <p>import pathlib<br>
  pathlib.Path(“output.md”).write_bytes(md_text.encode())</p>
  <p>import pymupdf4llm<br>
  llama_reader = pymupdf4llm.LlamaMarkdownReader()<br>
  llama_docs = llama_reader.load_data(“input.pdf”)</p>
  
  # topic_id
  
  166647
  
  # topic_title
  
  I have doubt in Q10

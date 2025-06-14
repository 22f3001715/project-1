- # id
  
  602167
  
  # username
  
  23f1002382
  
  # name
  
  Andrew David
  
  # post_url
  
  /t/solving-roe-realtime/168943/1
  
  # created_at
  
  2025-03-02T07:30:53.879Z
  
  # cooked
  
  <p>I’ll try to post whatever i solve lol XD</p>
  
  # topic_id
  
  168943
  
  # topic_title
  
  Solving ROE Realtime
- # id
  
  602183
  
  # username
  
  23f1002382
  
  # name
  
  Andrew David
  
  # post_url
  
  /t/solving-roe-realtime/168943/2
  
  # created_at
  
  2025-03-02T08:04:22.864Z
  
  # cooked
  
  <p>Q 7 LLM Embeddings (1 mark)</p>
  <p><strong>SecurePay</strong>, a leading fintech startup, has implemented an innovative feature to detect and prevent fraudulent activities in real time. As part of its security suite, the system analyzes personalized transaction messages by converting them into embeddings. These embeddings are compared against known patterns of legitimate and fraudulent messages to flag unusual activity.</p>
  <p>Imagine you are working on the SecurePay team as a junior developer tasked with integrating the text embeddings feature into the fraud detection module. When a user initiates a transaction, the system sends a personalized v…</p>
  <p>ANSWER:<br>
  {<br>
  “model”: “text-embedding-3-small”,<br>
  “input”: [<br>
  “Dear user, please verify your transaction code 33692 sent to roe-23f1002382@ds.study.iitm.ac.in”,<br>
  “Dear user, please verify your transaction code 66801 sent to roe-23f1002382@ds.study.iitm.ac.in”<br>
  ]<br>
  }</p>
  
  # topic_id
  
  168943
  
  # topic_title
  
  Solving ROE Realtime
- # id
  
  602184
  
  # username
  
  23f1002382
  
  # name
  
  Andrew David
  
  # post_url
  
  /t/solving-roe-realtime/168943/3
  
  # created_at
  
  2025-03-02T08:05:59.474Z
  
  # cooked
  
  <p>Q^: 6 Move and rename files (1 mark)</p>
  <p>Download q-move-rename-files.zip and extract it. Use <code>mv</code> to move all files under folders into an empty folder. Then rename all files replacing each digit with the next. 1 becomes 2, 9 becomes 0, <code>a1b9c.txt</code> becomes <code>a2b0c.txt</code>.</p>
  <p>ANSWER:</p>
  <pre><code class="lang-auto">unzip /workspaces/TDS/q-move-rename-files.zip -d extracted_folder123123
      5  mkdir empty_folder 
      6  find extracted_folder -type f -exec mv {} empty_folder/ \; 
      7  ls
      8  find extracted_folder123123 -type f -exec mv {} empty_folder/ \; 
      9  cd empty_folder  
     10  for file in *; do       new_name=$(echo "$file" | tr '0123456789' '1234567890')  ;     mv "$file" "$new_name"  ; done  
     11  grep . * | LC_ALL=C sort | sha256sum  
  </code></pre>
  
  # topic_id
  
  168943
  
  # topic_title
  
  Solving ROE Realtime
- # id
  
  602196
  
  # username
  
  23f1002382
  
  # name
  
  Andrew David
  
  # post_url
  
  /t/solving-roe-realtime/168943/4
  
  # created_at
  
  2025-03-02T08:13:44.624Z
  
  # cooked
  
  <p>Sydney,Brisbane,Perth,Jakarta,Singapore,Dubai,Doha<br>
  flights</p>
  
  # topic_id
  
  168943
  
  # topic_title
  
  Solving ROE Realtime
- # id
  
  602197
  
  # username
  
  23f1002382
  
  # name
  
  Andrew David
  
  # post_url
  
  /t/solving-roe-realtime/168943/5
  
  # created_at
  
  2025-03-02T08:14:15.471Z
  
  # cooked
  
  <p>150,171,174</p>
  <p>for studebts</p>
  
  # topic_id
  
  168943
  
  # topic_title
  
  Solving ROE Realtime

- # id
  
  594729
  
  # username
  
  vikramjncasr
  
  # name
  
  Vikram Suriyanarayanan
  
  # post_url
  
  /t/sudo-permission-needed-to-create-data-folder-in-root/167072/1
  
  # created_at
  
  2025-02-14T03:57:16.864Z
  
  # cooked
  
  <p><a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> sir please help</p>
  <p>When I am downloading the data folder after processing datagen.py , it is trying to download in root folder and it is facing permission error . how can we overcome this ?<br>
  needs sudo permission all the time…<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae.png" data-download-href="/uploads/short-url/yXVNx8O1oDleUm0YAE5Z6ZAElJk.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_690x70.png" alt="image" data-base62-sha1="yXVNx8O1oDleUm0YAE5Z6ZAElJk" width="690" height="70" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_690x70.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_1035x105.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f51040627e050b955bb243c23f1f660da36b73ae_2_1380x140.png 2x" data-dominant-color="1E2227"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2100×216 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  167072
  
  # topic_title
  
  Sudo permission needed to create data folder in root?
- # id
  
  594766
  
  # username
  
  carlton
  
  # name
  
  Carlton D'Silva
  
  # post_url
  
  /t/sudo-permission-needed-to-create-data-folder-in-root/167072/2
  
  # created_at
  
  2025-02-14T04:53:36.939Z
  
  # cooked
  
  <p>Hi Vikram,</p>
  <p>This is because (if you watched the session, or examined the code, you would have realised that) datagen.py was designed to run inside your docker container. And datagen.py (or a similar named file which we will not tell you ahead of time and will be provided as the query parameter in task A1) will normally be called by evaluate.py<br>
  Inside the docker container, permission for the data folder is set by the Dockerfile<br>
  which then allows your application to access the root folder inside your docker image and create the /data folder.</p>
  <p>So the workflow is like this (for your internal testing only… please follow the Project page for deliverables and evaluation to submit project successfully):</p>
  <ol>
  <li>You create your application server that serves 2 endpoints on localhost:8000</li>
  <li>You create a docker image that runs this application server.</li>
  <li>You run the docker image using podman as described in the project page.</li>
  <li>For mimicking the testing conditions. You need two files:<br>
  evaluate.py and datagen.py to be in the same folder where you are running these two scripts.</li>
  <li>Run evalute.py using uv.</li>
  </ol>
  <p>If your docker image is correctly configured and your application is correctly configured, then all the tasks run by evaluate.py will correctly tell you if the application is producing the right result for each task.</p>
  <p>Hope that gives clarity.</p>
  <p>Kind regards</p>
  
  # topic_id
  
  167072
  
  # topic_title
  
  Sudo permission needed to create data folder in root?

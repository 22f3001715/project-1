- # id
  
  619552
  
  # username
  
  24f2003130
  
  # name
  
  Shambhavi 
  
  # post_url
  
  /t/queries-regarding-end-term-exam-solutions/172707/1
  
  # created_at
  
  2025-04-15T09:59:51.136Z
  
  # cooked
  
  <p>Hi <a class="mention" href="/u/carlton">@carlton</a> and <a class="mention" href="/u/jivraj">@Jivraj</a> sir,</p>
  <p>I appeared for the end term examination held on 13th April 2025 during the FN shift. I would like to bring to your attention that the exam interface did not provide an option for multiple selections. However, a few questions appeared to have multiple correct answers.</p>
  <p>I have noted down the specific questions and the corresponding options I believe to be correct.So, kindly review them and let me know if there were any errors in my understanding of the questions. The questions are as follows:</p>
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8.jpeg" data-download-href="/uploads/short-url/A6rPaqEeHL4nw1GGBGp4tKdfWWs.jpeg?dl=1" title="1000042547" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_690x369.jpeg" alt="1000042547" data-base62-sha1="A6rPaqEeHL4nw1GGBGp4tKdfWWs" width="690" height="369" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_690x369.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8_2_1035x553.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/d/fd08e14665989ccea8f5a547b569521575208ae8.jpeg 2x" data-dominant-color="F0E8E6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042547</span><span class="informations">1080×578 187 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  <p>Question 2: Fields needed to filter “POST requests under /images/ from 15:00 to 18:00 on Mondays”</p>
  <p>To filter such logs, we need:</p>
  <p>Time → for the hour and the day (Monday)<br>
  Method → to filter POST<br>
  URL → to filter /images/</p>
  <p>So, the correct minimal set is:</p>
  <blockquote>
  <p><img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> Time, Method, URL</p>
  </blockquote>
  <p>Time → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
  Method → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
  URL → needed <img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"><br>
  Referer → not needed, but not harmful</p>
  <p>So this option includes all the necessary fields, just with one extra — which doesn’t invalidate it.</p>
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913.jpeg" data-download-href="/uploads/short-url/kBi3KxCTBUs9L4ifYXzDfQKdZRh.jpeg?dl=1" title="1000042548" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_690x192.jpeg" alt="1000042548" data-base62-sha1="kBi3KxCTBUs9L4ifYXzDfQKdZRh" width="690" height="192" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_690x192.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913_2_1035x288.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/0/9062a032d89a4b2b049ca34b23905d501cba7913.jpeg 2x" data-dominant-color="F5F3F2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042548</span><span class="informations">1080×301 71.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  <p>Acc to solutions only option 6406534159827 is valid:</p>
  <p>Status is numeric (200)<br>
  Method (GET), Protocol (HTTP/1.1), and URL (/index.html) are correct</p>
  <p>All required fields are present and properly formatted</p>
  <p>The other options were as follows:</p>
  <p>9825 uses invalid protocol (INVALID)</p>
  <p>9826 uses invalid status code (OK instead of numeric)</p>
  <p>9824 has no critical issue — it is technically also valid (only uses a private IP 192.168.1.1, which is unusual but not invalid). So both 9824 and 9827 are valid, but the answer marked only 9827</p>
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373.jpeg" data-download-href="/uploads/short-url/wzS0A3Uz9s9vYMNHAkB3yKh7cn.jpeg?dl=1" title="1000042545" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_690x299.jpeg" alt="1000042545" data-base62-sha1="wzS0A3Uz9s9vYMNHAkB3yKh7cn" width="690" height="299" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_690x299.jpeg, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373_2_1035x448.jpeg 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/0/3/03aec49b7ba39078f204ef24fefa80dae8e9b373.jpeg 2x" data-dominant-color="F7F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1000042545</span><span class="informations">1079×468 35.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
  Correct Answer(s):</p>
  <p><img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> PUT – Correct: It replaces the resource entirely. Multiple identical PUTs = same result.</p>
  <p><img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> GET – Also correct: It only fetches data, no side-effects. Multiple GETs = same result.</p>
  <p><img src="https://emoji.discourse-cdn.com/google/white_check_mark.png?v=14" title=":white_check_mark:" class="emoji" alt=":white_check_mark:" loading="lazy" width="20" height="20"> DELETE – Technically correct: Deleting the same resource multiple times has the same result as deleting once (resource stays deleted).</p>
  <hr>
  <p>Incorrect Answer:</p>
  <p><img src="https://emoji.discourse-cdn.com/google/cross_mark.png?v=14" title=":cross_mark:" class="emoji" alt=":cross_mark:" loading="lazy" width="20" height="20"> POST – Not idempotent. Each POST usually creates a new resource or changes server state.</p>
  <p>(This is the mistake on my part that I put the ans as POST as I thought since 3/4 are idempotent and one is not I should select the odd one out but I hope this could be resolved)</p>
  <p>Thank you</p>
  
  # topic_id
  
  172707
  
  # topic_title
  
  Queries regarding End Term exam solutions
- # id
  
  619868
  
  # username
  
  koustubhr
  
  # name
  
  Koustubh Ramakrishnan
  
  # post_url
  
  /t/queries-regarding-end-term-exam-solutions/172707/2
  
  # created_at
  
  2025-04-15T17:19:29.506Z
  
  # cooked
  
  <p>Agree &amp; second all thoughts shared by <a class="mention" href="/u/24f2003130">@24f2003130</a> above.</p>
  <ul>
  <li>
  <p>I also wanted to clarify on this question on filtered entries. The question mentions that a list filtered_entries is being created , and with the way the question is structured it seems like the filtering conditions mentioned in the question have already been applied. In that case <code>len(filtered entries)</code> seems to be correct. However the right answer is marked ‘None of these’ .<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0.png" data-download-href="/uploads/short-url/z5Qvydw8nYEYuIyQ5RZLKdwMgzS.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_690x245.png" alt="image" data-base62-sha1="z5Qvydw8nYEYuIyQ5RZLKdwMgzS" width="690" height="245" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_690x245.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0_2_1035x367.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/5/f5f549e906df1006709b3257742fff4b52f416d0.png 2x" data-dominant-color="F2EFEE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1108×394 81.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  </li>
  <li>
  <p>The valid log entry had me stumped too, option 1 and 4 both look absolutely fine yet only option 4 is marked correct.</p>
  </li>
  <li>
  <p>Also, only POST request is not idempotent, all other requests are idempotent yet only PUT is marked correct.</p>
  </li>
  </ul>
  <p>Request you to please clarify and consider these points.</p>
  
  # topic_id
  
  172707
  
  # topic_title
  
  Queries regarding End Term exam solutions
- # id
  
  619891
  
  # username
  
  22f3000819
  
  # name
  
  Shivaditya Bhattacharya
  
  # post_url
  
  /t/queries-regarding-end-term-exam-solutions/172707/3
  
  # created_at
  
  2025-04-15T18:13:03.725Z
  
  # cooked
  
  <p>Yes <a class="mention" href="/u/carlton">@carlton</a> the wording of the question made it seem like the filters were already applied on the list <code>filtered_entries</code>.</p>
  
  # topic_id
  
  172707
  
  # topic_title
  
  Queries regarding End Term exam solutions

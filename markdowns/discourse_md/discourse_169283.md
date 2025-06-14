- # id
  
  603963
  
  # username
  
  Jivraj
  
  # name
  
  Jivraj Singh Shekhawat
  
  # post_url
  
  /t/graded-assignment-6/169283/1
  
  # created_at
  
  2025-03-06T13:48:39.245Z
  
  # cooked
  
  <p>Please post any questions related to <a href="https://seek.onlinedegree.iitm.ac.in/courses/ns_25t1_se2002?id=25&amp;type=assignment&amp;tab=courses&amp;unitId=23">Graded Assignment 6 - Data Analysis</a></p>
  <p>Please use markdown code formatting (fenced code blocks) when sharing code (rather than screenshots). It’s easier for us to copy-paste and test.</p>
  <p>Deadline <span class="discourse-local-date" data-date="2025-03-16" data-email-preview="2025-03-15T18:30:00Z UTC" data-timezone="Asia/Calcutta">2025-03-15T18:30:00Z</span></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  603964
  
  # username
  
  Jivraj
  
  # name
  
  Jivraj Singh Shekhawat
  
  # post_url
  
  /t/graded-assignment-6/169283/2
  
  # created_at
  
  2025-03-06T13:49:29.690Z
  
  # cooked
  
  
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  603966
  
  # username
  
  24f2006061
  
  # name
  
  Lovepreet Singh
  
  # post_url
  
  /t/graded-assignment-6/169283/3
  
  # created_at
  
  2025-03-02T11:45:12.668Z
  
  # cooked
  
  <p>The answer choices for questions 1 and 2 in graded assignment 6 are quite confusing. Both questions are single-select, yet three out of the four options are correct in each case. I’m unsure whether to choose one of the correct options or if the question is actually asking for the incorrect one. Could someone please clarify?</p>
  <p><a class="mention" href="/u/carlton">@carlton</a></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  602355
  
  # username
  
  23f2005138
  
  # name
  
  Sarang Tambe
  
  # post_url
  
  /t/graded-assignment-6/169283/4
  
  # created_at
  
  2025-03-02T11:57:04.636Z
  
  # cooked
  
  <p><a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
  I have similar concern<br>
  For Q1, I used the following code:</p>
  <pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Karnataka between price retention and column')
  kk = df[df['State'] == 'Karnataka']
  for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
      pearson_corr = kk['price_retention'].corr(kk[col])
      print(f'\t{col:25} : {pearson_corr:.2f}')
  </code></pre>
  <p>And got the following output:</p>
  <pre><code class="lang-auto">Pearson correlation for Karnataka between price retention and column
  	Mileage (km/l)            : 0.03
  	Avg Daily Distance (km)   : -0.06
  	Engine Capacity (cc)      : -0.04
  </code></pre>
  <p>Whereas options are below where none of them are correct.<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" data-download-href="/uploads/short-url/nPaaIWtriJMunrro5mxPkkzgs0I.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/a/6/a6fa9a2e601c94da84cbd25c406235d1009b204c.png" alt="image" data-base62-sha1="nPaaIWtriJMunrro5mxPkkzgs0I" width="281" height="219"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">281×219 9.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  <p>Whereas for Q2 (Punjab and Yamaha) I used the following code:</p>
  <pre data-code-wrap="python"><code class="lang-python">print(f'Pearson correlation for Punjab and Yamaha between price retention and column')
  pb = df[(df['State'] == 'Punjab') &amp; (df['Brand'] == 'Yamaha')]
  for col in ['Mileage (km/l)', 'Avg Daily Distance (km)', 'Engine Capacity (cc)']:
      pearson_corr = pb['price_retention'].corr(pb[col])
      print(f'\t{col:25} : {pearson_corr:.2f}')
  </code></pre>
  <p>and got the following answers:</p>
  <pre><code class="lang-auto">Pearson correlation for Punjab and Yamaha between price retention and column
  	Mileage (km/l)            : 0.24
  	Avg Daily Distance (km)   : -0.06
  	Engine Capacity (cc)      : -0.08
  </code></pre>
  <p>The options for Q2 are given below and 2 of them are correct (AvgDistance and Mileage).<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" data-download-href="/uploads/short-url/bEEgmsyChZ5YyAlqcLdD1S91PE2.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/5/1/51b03d00c3e962e6c4fc7fc64930a23e82500006.png" alt="image" data-base62-sha1="bEEgmsyChZ5YyAlqcLdD1S91PE2" width="278" height="216"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">278×216 9.19 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  603367
  
  # username
  
  carlton
  
  # name
  
  Carlton D'Silva
  
  # post_url
  
  /t/graded-assignment-6/169283/5
  
  # created_at
  
  2025-03-04T10:11:22.975Z
  
  # cooked
  
  <p><a class="mention" href="/u/24f2006061">@24f2006061</a> We are looking into it. We will update based on our analysis. Thanks for letting us know.</p>
  <p>Kind regards</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  603970
  
  # username
  
  AbhinavOhri
  
  # name
  
  Abhinav
  
  # post_url
  
  /t/graded-assignment-6/169283/6
  
  # created_at
  
  2025-03-03T18:06:51.395Z
  
  # cooked
  
  <p>I used a python script to get the solution to quesiton 1 of week 6 graded assignment. It matches three options. Is this a bug or like we then need to analyze using the pearson coefficient to determine which option is the correct one<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630.png" data-download-href="/uploads/short-url/qYtCOu4iFTJRgTpq1aybIwZqRVe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png" alt="image" data-base62-sha1="qYtCOu4iFTJRgTpq1aybIwZqRVe" width="690" height="131" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_690x131.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_1035x196.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/b/d/bd0ea5ffab782a7d6bcc8b1cde7ba7f385b85630_2_1380x262.png 2x" data-dominant-color="FAF9FA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1383×263 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  604313
  
  # username
  
  24ds3000090
  
  # name
  
  Wasim Ansari
  
  # post_url
  
  /t/graded-assignment-6/169283/7
  
  # created_at
  
  2025-03-07T17:12:28.199Z
  
  # cooked
  
  <p>Dear Sirs, Can we have some response on these issues related particularly to the questions 1 and 2 of Graded Assignment 6. It looks like multiple options are correct in the given options. Any guidance or hint, on how to arrive at the right answer will be helpful. Thanks and regards. <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  604590
  
  # username
  
  23f2003413
  
  # name
  
  Shashannk
  
  # post_url
  
  /t/graded-assignment-6/169283/8
  
  # created_at
  
  2025-03-08T15:17:03.743Z
  
  # cooked
  
  <p>Yeah…Even I am facing the same issue. Out of the 4 options provided, 3 options are correct in my case both for Q1 &amp; Q2, but both these questions are single-choice questions. Kindly look into it and help us out <a class="mention" href="/u/carlton">@carlton</a> !</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605292
  
  # username
  
  23ds2000092
  
  # name
  
  RAJ K BOOPATHI
  
  # post_url
  
  /t/graded-assignment-6/169283/9
  
  # created_at
  
  2025-03-10T07:56:14.493Z
  
  # cooked
  
  <p>I guess for both Q1 &amp; Q2, we need to find the option that is having stronger correlation (positive/negative). Please correct me if I am wrong.</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605551
  
  # username
  
  21f2000709
  
  # name
  
  Pradeep Mondal
  
  # post_url
  
  /t/graded-assignment-6/169283/10
  
  # created_at
  
  2025-03-11T06:42:12.463Z
  
  # cooked
  
  <p>Any updates on these? I am too facing the same issue.</p>
  <p><a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605753
  
  # username
  
  Udipth
  
  # name
  
  Udipth
  
  # post_url
  
  /t/graded-assignment-6/169283/11
  
  # created_at
  
  2025-03-11T17:42:32.616Z
  
  # cooked
  
  <p>In GA6 for first 2 questions 3 out of 4 options are correct. Even the question is not clearly asking anything. Kindly suggest are we supposed to select the wrong one<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04.png" data-download-href="/uploads/short-url/A4m6gPBqXgQhJ3fsG8iEiLd5pKQ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png" alt="image" data-base62-sha1="A4m6gPBqXgQhJ3fsG8iEiLd5pKQ" width="690" height="190" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_690x190.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_1035x285.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/f/c/fccc54e8cff0595d93b1c5185ce0a10343849b04_2_1380x380.png 2x" data-dominant-color="F8F8F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2083×575 47.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605798
  
  # username
  
  23f2003413
  
  # name
  
  Shashannk
  
  # post_url
  
  /t/graded-assignment-6/169283/12
  
  # created_at
  
  2025-03-12T03:42:05.053Z
  
  # cooked
  
  <p>Kindly update us regarding the status of Q1 &amp; Q2 <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a></p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605954
  
  # username
  
  lakshaygarg654
  
  # name
  
  LAKSHAY
  
  # post_url
  
  /t/graded-assignment-6/169283/13
  
  # created_at
  
  2025-03-12T11:29:04.042Z
  
  # cooked
  
  <p><a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
  Dear TDS Team,</p>
  <p>There are multiple issues in Graded Assignment 6 that require urgent attention:</p>
  <ol>
  <li>Questions 1 and 2, along with their options, are ambiguous.</li>
  <li>In Questions 3 and 4, I am unable to obtain an exact answer that matches any of the given options, despite trying multiple approaches, including the Excel regression method and other models in a Google Colab file.</li>
  <li>The data for Question 10 is missing. I attempted to run the shapefile in QGIS, but it resulted in an error. Additionally, I searched for the shapefile of New York roads on official websites, but their servers are currently under maintenance.</li>
  </ol>
  <p>The assignment deadline is approaching, but these issues remain unresolved. Kindly look into this matter at the earliest and provide a resolution as soon as possible.</p>
  <p>Thank you for your support.</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  605995
  
  # username
  
  21f2000709
  
  # name
  
  Pradeep Mondal
  
  # post_url
  
  /t/graded-assignment-6/169283/14
  
  # created_at
  
  2025-03-12T13:30:00.912Z
  
  # cooked
  
  <p>Yes, there are no specifics in Q1 to Q4 and are quite ambiguous.</p>
  <p>For instance:</p>
  <blockquote>
  <p>forecast the 2027 resale value of the Hero - HF Deluxe in Gujarat, using historical data.</p>
  </blockquote>
  <p>but is this talking about the average resale value as no input features are specified?</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606007
  
  # username
  
  lakshaygarg654
  
  # name
  
  LAKSHAY
  
  # post_url
  
  /t/graded-assignment-6/169283/15
  
  # created_at
  
  2025-03-12T14:11:15.210Z
  
  # cooked
  
  <p>Let’s wait for their response.<br>
  I submitted nearby option for Q3 and Q4</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606017
  
  # username
  
  23f3001745
  
  # name
  
  Vivek Rekha Ashoka
  
  # post_url
  
  /t/graded-assignment-6/169283/16
  
  # created_at
  
  2025-03-12T14:36:43.739Z
  
  # cooked
  
  <p><a class="mention" href="/u/jivraj">@Jivraj</a> <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/saransh_saini">@Saransh_Saini</a><br>
  Can you please provide any update ASAP as the deadline for this GA coincides with Quiz 2. With many ambiguities unresolved it’s hard to solve this and study for Quiz 2 (and do offline college work even though that’s not your problem).<br>
  Thanks</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606228
  
  # username
  
  Jivraj
  
  # name
  
  Jivraj Singh Shekhawat
  
  # post_url
  
  /t/graded-assignment-6/169283/17
  
  # created_at
  
  2025-03-13T09:47:03.906Z
  
  # cooked
  
  <p>Hi <span class="mention">@all</span></p>
  <p>Question intends you to select most correlated one.<br>
  Select option which is absolute highest.</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606558
  
  # username
  
  Sunil_mv
  
  # name
  
  M v Sunil
  
  # post_url
  
  /t/graded-assignment-6/169283/18
  
  # created_at
  
  2025-03-14T14:30:12.725Z
  
  # cooked
  
  <p><a class="mention" href="/u/jivraj">@Jivraj</a>  - Can you please check answer choices for Q7 for GA6 where no choices are matching with the answer. The answer is coming to around 11.5 kms which is 11500 meters.<br>
  Q.A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Pine Pines Junction : (26.5596,-99.5336) ;Maple Fields Station : (26.4212,-99.4597);South Glen Crossing : (26.5962,-99.5243);Cedar Creek Retreat : (26.56,-99.4519) &amp; Central Command Post Location: (26.4644,-99.4771) Using the Haversine package, calculate the distance from the Central Command Post to Pine Pines Junction. Which of the following is the MOST ACCURATE distance</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606603
  
  # username
  
  23f3001601
  
  # name
  
  Shashank Tripathi
  
  # post_url
  
  /t/graded-assignment-6/169283/19
  
  # created_at
  
  2025-03-14T16:06:48.081Z
  
  # cooked
  
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png" data-download-href="/uploads/short-url/lrXmd4rKqCvHw9vxjDwssxhuPML.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png" alt="image" data-base62-sha1="lrXmd4rKqCvHw9vxjDwssxhuPML" width="690" height="197" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_690x197.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b_2_1035x295.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/9/6/9656b143021a1b4baf78510b1ba05ae9cbd6ca9b.png 2x" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1318×377 34.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
  what to do if 3 options have same value -0.04 and all are correct?</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6
- # id
  
  606761
  
  # username
  
  23f2005471
  
  # name
  
  Khushi Shah
  
  # post_url
  
  /t/graded-assignment-6/169283/20
  
  # created_at
  
  2025-03-15T05:54:10.148Z
  
  # cooked
  
  <p><a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/jivraj">@Jivraj</a><br>
  My question 7 for GA6 is :<br>
  A wildfire is threatening a rural mountain region, and emergency services need to coordinate evacuation routes for four remote communities. The Emergency Management Center is located at a central command post, and must plan the most efficient evacuation route to ensure rapid and safe community evacuation. The four communities are: Silver Springs Community : (42.1029,-85.665) ;Pleasant Harbor Community : (42.1238,-85.9043);Summit Shores Village : (42.0415,-85.8696);River Retreat Outpost : (42.0417,-85.6836) &amp; Central Command Post Location: (42.0587,-85.7226) Using the Haversine package, calculate the distance from the Central Command Post to Silver Springs Community. Which of the following is the MOST ACCURATE distance<br>
  Whose options provided are :<br>
  10418 meters</p>
  <p>12287 meters</p>
  <p>10965 meters</p>
  <p>11149 meters</p>
  <p>However, after trying all methods out there my distance comes out to be 6873 meters, I selected 10418 as the answer (closest approximation to 6873 meters)</p>
  <p>I assume that the question must have been central command post to summit shores village (whose answer turns out to be 12287 meters)<br>
  Kindly look into the question, and let me know about the same (the destination from central command post)</p>
  
  # topic_id
  
  169283
  
  # topic_title
  
  Graded assignment 6

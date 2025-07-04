- # id
  
  596311
  
  # username
  
  21f3002647
  
  # name
  
  Arnav Mehta 
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/1
  
  # created_at
  
  2025-02-17T10:07:56.783Z
  
  # cooked
  
  <p>Dear TDS Team,</p>
  <p>I have verified my submission, and my repository <strong>does include a Dockerfile</strong>, and the <strong>Docker image is accessible on DockerHub</strong>. Please find the attached screenshot as proof. Kindly review my submission again and let me know if any further action is needed.</p>
  <p>Looking forward to your confirmation.</p>
  <p>Best regards,<br>
  Arnav Mehta<br>
  (21f3002647)</p>
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png" data-download-href="/uploads/short-url/fahuMqTlIDS9GwNGNM399QrBKhJ.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png" alt="image" data-base62-sha1="fahuMqTlIDS9GwNGNM399QrBKhJ" width="234" height="500" data-dominant-color="161A21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">250×534 3.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/1/d14c53cce65e7ac7f679de75bba301f3ee23f1f0.png" data-download-href="/uploads/short-url/tRxjXpqC5mBAEB7FLLzaX0j5ccg.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/d/1/d14c53cce65e7ac7f679de75bba301f3ee23f1f0.png" alt="image" data-base62-sha1="tRxjXpqC5mBAEB7FLLzaX0j5ccg" width="690" height="230" data-dominant-color="1D242C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">713×238 11 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596337
  
  # username
  
  21f3002647
  
  # name
  
  Arnav Mehta 
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/2
  
  # created_at
  
  2025-02-17T12:30:15.244Z
  
  # cooked
  
  <p><a class="mention" href="/u/saransh_saini">@Saransh_Saini</a> sir what should i do?</p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596404
  
  # username
  
  Saransh_Saini
  
  # name
  
  Saransh Saini
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/3
  
  # created_at
  
  2025-02-17T15:43:39.614Z
  
  # cooked
  
  <p><a class="mention" href="/u/carlton">@carlton</a> Kindly have a look into this.</p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596467
  
  # username
  
  satviksawhney
  
  # name
  
  Satvik  Sawhney
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/8
  
  # created_at
  
  2025-02-18T00:48:03.881Z
  
  # cooked
  
  <p>Good Morning Sir,<br>
  Sir even I am facing a similar issue, even though sanity check for docker image on docker hub was cleared but got a mail saying ‘dockerfile’ not present in the GitHub repo while it clearly was. Sir please look into it we have given so many days to complete this project.</p>
  <p>Looking forward to your reply.</p>
  <p>Thank you<br>
  Satvik Sawhney<br>
  23f2003680</p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596517
  
  # username
  
  carlton
  
  # name
  
  Carlton D'Silva
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/9
  
  # created_at
  
  2025-02-18T05:00:31.191Z
  
  # cooked
  
  <p>So the reason for the failure is:</p>
  <p>You had initially put your Dockerfile inside a directory called TDSP-1-main instead of being directly in your repo. (On 15th Feb 1:26AM)</p>
  <p>Then when our automated script checked if students repos met the requirements and yours did not we immediately sent out a warning email as a opportunity for students to make the necessary corrections.</p>
  <p>Then once you realised your mistake, on <strong>Feb 17th at 9:11 pm IST</strong> i.e <em>yesteday</em>, you changed your repo to put the files in the correct locations.</p>
  <p>Then you finally posted here on Discourse with the image [quote=“21f3002647, post:1, topic:167471”]<br>
  <div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png" data-download-href="/uploads/short-url/fahuMqTlIDS9GwNGNM399QrBKhJ.png?dl=1" title="image"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/6/a/6a4a28aa638840e8d2e4dbf246ca235fd41e5ccb.png" alt="image" data-base62-sha1="fahuMqTlIDS9GwNGNM399QrBKhJ" width="234" height="500" data-dominant-color="161A21"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">250×534 3.92 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
  [/quote]</p>
  <p>showing that your files are in the correct place.</p>
  <p>We do not take into consideration modifications to your repo after the deadline because then we would have to extend that curtesy to all students.</p>
  <p>Kind regards</p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596587
  
  # username
  
  21f3002647
  
  # name
  
  Arnav Mehta 
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/10
  
  # created_at
  
  2025-02-18T06:35:49.560Z
  
  # cooked
  
  <p><a class="mention" href="/u/carlton">@carlton</a> sir<br>
  Yes, I corrected my repo at 9:11 PM IST, but I had actually written and submitted my query much earlier at 4 PM. At that time, I wasn’t entirely sure if this was the actual issue, but it looks like it was.</p>
  <p>I understand that the deadline had already passed, and I only saw the email later. I had two GATE papers on the 15th and an interview on the 16th, so I was extremely busy and couldn’t check my emails sooner. However, I had raised my concern well before making the correction, so I’d really appreciate it if my submission could still be considered <img src="https://emoji.discourse-cdn.com/google/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"></p>
  <p>Kind regards,<br>
  Arnav Mehta<br>
  21f3002647</p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image
- # id
  
  596639
  
  # username
  
  satviksawhney
  
  # name
  
  Satvik  Sawhney
  
  # post_url
  
  /t/project-1-submission-marked-as-fail-despite-having-dockerfile-image/167471/11
  
  # created_at
  
  2025-02-18T08:28:16.577Z
  
  # cooked
  
  <p>Sir, please consider it we have spent a lot of time, in my case just the d in Dockerfile was small that too on remote repository. On my local repository it was Dockerfile only I even have a published docker image as verified by you autated script only. The name of the file on remote repository did not change even after commit it through my local repo, once I read the mail in morning it was only then I realised it wasn’t changed on GitHub repo.</p>
  <p>Sir I understand the deadline has passed and I am not asking for a resubmission, I am just asking to consider the already submitted work, just that. It would be really helpful. I just have one commit on my repo that too “Rename dockerfile to Dokerfile” . Sir please attest consider what we have already submitted. I have made no changes as you can verify it too.</p>
  <p>Sir it is a humble request to please consider it.</p>
  <p>Warm Regards,<br>
  Satvik Sawhney<br>
  23f2003680</p>
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d.png" data-download-href="/uploads/short-url/3Lil8Qu84E3T6jREDGJRO6bakiN.png?dl=1" title="Screenshot 2025-02-18 at 1.53.10 PM" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d_2_690x170.png" alt="Screenshot 2025-02-18 at 1.53.10 PM" data-base62-sha1="3Lil8Qu84E3T6jREDGJRO6bakiN" width="690" height="170" srcset="https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d_2_690x170.png, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d_2_1035x255.png 1.5x, https://europe1.discourse-cdn.com/flex013/uploads/iitm/optimized/3X/1/a/1a5f2ea044383efcb5d248ddb487665e9e65957d_2_1380x340.png 2x" data-dominant-color="15181D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2025-02-18 at 1.53.10 PM</span><span class="informations">1889×467 54 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
  
  # topic_id
  
  167471
  
  # topic_title
  
  Project 1 Submission Marked as FAIL Despite Having Dockerfile & Image

- # id
  
  598100
  
  # username
  
  muskan2431
  
  # name
  
  Muskan Aggarwal
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/1
  
  # created_at
  
  2025-02-21T18:32:17.871Z
  
  # cooked
  
  <p><div class="lightbox-wrapper"><a class="lightbox" href="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/158680f0acc5ef430efd87e8a1cc59a78e6d5e07.png" data-download-href="/uploads/short-url/34qcnwBcLwmxZulqWMVZUZGT9gX.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://europe1.discourse-cdn.com/flex013/uploads/iitm/original/3X/1/5/158680f0acc5ef430efd87e8a1cc59a78e6d5e07.png" alt="image" data-base62-sha1="34qcnwBcLwmxZulqWMVZUZGT9gX" width="690" height="352" data-dominant-color="F5F5F5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1337×683 31.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
  It seems that the question in <em>Graded Assignment 5 for TDS</em> is producing incorrect results despite the same logic working correctly for other variations of the problem. Please check into this question once as I have cross checked with many of the students and chatgpt and all of us faced  this issue in this question. Thanks!<br>
  <a class="mention" href="/u/carlton">@carlton</a> <a class="mention" href="/u/s.anand">@s.anand</a></p>
  <p>code to take reference from:</p>
  <pre><code class="lang-auto">import gzip
  import pandas as pd
  from datetime import datetime
  
  log_path = 's-anand.net-May-2024.gz'
  start_time = datetime.strptime('01:00:00', '%H:%M:%S').time()
  end_time = datetime.strptime('15:00:00', '%H:%M:%S').time()
  log_data = []
  
  def parse_log(line):
      parts = line.split(' ')
      log_time = datetime.strptime(parts[3][1:], '%d/%b/%Y:%H:%M:%S')
      method, url, status = parts[5][1:], parts[6], int(parts[8])
      return log_time, method, url, status
  
  with gzip.open(log_path, 'rt') as file:
      for entry in file:
          log_time, method, url, status = parse_log(entry)
          if method == 'GET' and url.startswith('/blog/') and 200 &lt;= status &lt; 300:
              if log_time.weekday() == 0 and start_time &lt;= log_time.time() &lt; end_time:
                  log_data.append(entry)
  
  print(f"Successful GET requests: {len(log_data)}")
  </code></pre>
  <p>ps: I shared code after the deadline hopefully no issues there! <img src="https://emoji.discourse-cdn.com/google/laughing.png?v=12" title=":laughing:" class="emoji" alt=":laughing:" loading="lazy" width="20" height="20"></p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  598177
  
  # username
  
  amitchaurasia
  
  # name
  
  Amit
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/4
  
  # created_at
  
  2025-02-22T04:08:00.787Z
  
  # cooked
  
  <p>I’m also facing same kind of issue in Q3, GA5, while cross checked answer from different methods getting same result 1603, which is showing incorrect.<br>
  Kindly check this issue.<br>
  Thanks</p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  598240
  
  # username
  
  Aryxn
  
  # name
  
  Aryan Singh
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/5
  
  # created_at
  
  2025-02-22T05:52:55.677Z
  
  # cooked
  
  <p>The same issue is being faced by many students, not only for this condition, but others as well. Please look into it</p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  598344
  
  # username
  
  23f2000573
  
  # name
  
  B R GIRI SUBRAHMANYA
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/6
  
  # created_at
  
  2025-02-22T08:28:29.532Z
  
  # cooked
  
  <p>actually i got 130 as answer. but the answer accepted by the portal was 129. i felt like, i have to change one or two numbers front and back, i tried the same before. it worked <img src="https://emoji.discourse-cdn.com/google/sweat_smile.png?v=12" title=":sweat_smile:" class="emoji" alt=":sweat_smile:" loading="lazy" width="20" height="20"></p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  598383
  
  # username
  
  muskan2431
  
  # name
  
  Muskan Aggarwal
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/7
  
  # created_at
  
  2025-02-22T09:57:39.167Z
  
  # cooked
  
  <p>For the same question? But it shouldnt be +1 -1 to get the correct answer right.</p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  598948
  
  # username
  
  carlton
  
  # name
  
  Carlton D'Silva
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/8
  
  # created_at
  
  2025-02-24T11:48:02.411Z
  
  # cooked
  
  <p>Hi <a class="mention" href="/u/muskan2431">@muskan2431</a> we are running some checks.</p>
  <p>Please bear with us,<br>
  Kind regards</p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer
- # id
  
  599493
  
  # username
  
  carlton
  
  # name
  
  Carlton D'Silva
  
  # post_url
  
  /t/q3-ga5-not-accepting-right-answer/168011/9
  
  # created_at
  
  2025-02-25T11:13:32.454Z
  
  # cooked
  
  <p>We have determined that some students were affected by GA5 Q3. Whoever we have identified as having received the incorrect assessment will receive 1 mark for that particular question. These are the students that we have identified as been assessed incorrectly:</p>
  <div class="md-table">
  <table>
  <thead>
  <tr>
  <th>SN</th>
  <th>Email</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td>1</td>
  <td>21f1000131@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>2</td>
  <td>21f1001484@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>3</td>
  <td>21f1001631@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>4</td>
  <td>21f1001729@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>5</td>
  <td>21f1001890@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>6</td>
  <td>21f1002734@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>7</td>
  <td>21f1002773@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>8</td>
  <td>21f1003135@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>9</td>
  <td>21f1003475@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>10</td>
  <td>21f1003816@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>11</td>
  <td>21f1005422@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>12</td>
  <td>21f1005510@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>13</td>
  <td>21f1006234@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>14</td>
  <td>21f1006309@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>15</td>
  <td>21f1006867@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>16</td>
  <td>21f2000525@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>17</td>
  <td>21f2000913@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>18</td>
  <td>21f2000998@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>19</td>
  <td>21f2001061@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>20</td>
  <td>21f2001080@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>21</td>
  <td>21f2001543@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>22</td>
  <td>21f3000311@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>23</td>
  <td>21f3000355@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>24</td>
  <td>21f3000512@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>25</td>
  <td>21f3000591@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>26</td>
  <td>21f3000687@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>27</td>
  <td>21f3000813@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>28</td>
  <td>21f3001091@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>29</td>
  <td>21f3001161@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>30</td>
  <td>21f3001936@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>31</td>
  <td>21f3001965@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>32</td>
  <td>21f3002158@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>33</td>
  <td>21f3002431@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>34</td>
  <td>21f3002444@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>35</td>
  <td>21f3002647@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>36</td>
  <td>21f3002782@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>37</td>
  <td>21f3003195@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>38</td>
  <td>22ds2000011@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>39</td>
  <td>22f1000376@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>40</td>
  <td>22f1000821@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>41</td>
  <td>22f1000902@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>42</td>
  <td>22f1000935@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>43</td>
  <td>22f1000989@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>44</td>
  <td>22f1001095@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>45</td>
  <td>22f1001316@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>46</td>
  <td>22f1001391@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>47</td>
  <td>22f1001416@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>48</td>
  <td>22f1001438@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>49</td>
  <td>22f1001542@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>50</td>
  <td>22f1001551@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>51</td>
  <td>22f1001552@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>52</td>
  <td>22f1001862@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>53</td>
  <td>22f2000108@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>54</td>
  <td>22f2000113@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>55</td>
  <td>22f2000116@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>56</td>
  <td>22f2000273@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>57</td>
  <td>22f2000467@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>58</td>
  <td>22f2000813@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>59</td>
  <td>22f2000898@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>60</td>
  <td>22f2000946@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>61</td>
  <td>22f2001041@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>62</td>
  <td>22f2001336@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>63</td>
  <td>22f2001532@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>64</td>
  <td>22f2001590@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>65</td>
  <td>22f3000275@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>66</td>
  <td>22f3000337@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>67</td>
  <td>22f3000419@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>68</td>
  <td>22f3000422@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>69</td>
  <td>22f3000487@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>70</td>
  <td>22f3000563@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>71</td>
  <td>22f3000694@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>72</td>
  <td>22f3000814@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>73</td>
  <td>22f3000819@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>74</td>
  <td>22f3000831@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>75</td>
  <td>22f3000833@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>76</td>
  <td>22f3001050@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>77</td>
  <td>22f3001074@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>78</td>
  <td>22f3001108@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>79</td>
  <td>22f3001278@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>80</td>
  <td>22f3001316@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>81</td>
  <td>22f3001675@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>82</td>
  <td>22f3001688@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>83</td>
  <td>22f3001777@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>84</td>
  <td>22f3001834@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>85</td>
  <td>22f3001930@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>86</td>
  <td>22f3001961@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>87</td>
  <td>22f3001967@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>88</td>
  <td>22f3002011@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>89</td>
  <td>22f3002175@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>90</td>
  <td>22f3002184@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>91</td>
  <td>22f3002236@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>92</td>
  <td>22f3002265@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>93</td>
  <td>22f3002291@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>94</td>
  <td>22f3002307@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>95</td>
  <td>22f3002394@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>96</td>
  <td>22f3002447@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>97</td>
  <td>22f3002498@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>98</td>
  <td>22f3002565@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>99</td>
  <td>22f3002634@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>100</td>
  <td>22f3002712@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>101</td>
  <td>22f3002813@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>102</td>
  <td>22f3002844@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>103</td>
  <td>22f3002948@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>104</td>
  <td>22f3003003@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>105</td>
  <td>22f3003237@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>106</td>
  <td>23ds1000032@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>107</td>
  <td>23ds2000055@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>108</td>
  <td>23ds2000069@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>109</td>
  <td>23ds3000146@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>110</td>
  <td>23ds3000149@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>111</td>
  <td>23ds3000224@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>112</td>
  <td>23f1000232@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>113</td>
  <td>23f1000257@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>114</td>
  <td>23f1000292@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>115</td>
  <td>23f1000587@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>116</td>
  <td>23f1000776@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>117</td>
  <td>23f1000813@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>118</td>
  <td>23f1000844@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>119</td>
  <td>23f1001472@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>120</td>
  <td>23f1001651@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>121</td>
  <td>23f1001684@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>122</td>
  <td>23f1001788@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>123</td>
  <td>23f1001861@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>124</td>
  <td>23f1002075@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>125</td>
  <td>23f1002114@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>126</td>
  <td>23f1002279@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>127</td>
  <td>23f1002345@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>128</td>
  <td>23f1002362@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>129</td>
  <td>23f1002535@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>130</td>
  <td>23f1002563@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>131</td>
  <td>23f1002586@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>132</td>
  <td>23f1002630@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>133</td>
  <td>23f1002929@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>134</td>
  <td>23f1003000@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>135</td>
  <td>23f1003115@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>136</td>
  <td>23f2000119@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>137</td>
  <td>23f2000273@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>138</td>
  <td>23f2000762@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>139</td>
  <td>23f2000794@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>140</td>
  <td>23f2000822@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>141</td>
  <td>23f2000926@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>142</td>
  <td>23f2000942@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>143</td>
  <td>23f2001274@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>144</td>
  <td>23f2001347@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>145</td>
  <td>23f2001494@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>146</td>
  <td>23f2001529@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>147</td>
  <td>23f2001539@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>148</td>
  <td>23f2001661@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>149</td>
  <td>23f2001960@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>150</td>
  <td>23f2001992@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>151</td>
  <td>23f2002034@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>152</td>
  <td>23f2002121@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>153</td>
  <td>23f2002865@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>154</td>
  <td>23f2002939@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>155</td>
  <td>23f2003529@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>156</td>
  <td>23f2003751@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>157</td>
  <td>23f2003893@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>158</td>
  <td>23f2004115@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>159</td>
  <td>23f2004244@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>160</td>
  <td>23f2004366@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>161</td>
  <td>23f2004443@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>162</td>
  <td>23f2004473@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>163</td>
  <td>23f2004510@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>164</td>
  <td>23f2004637@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>165</td>
  <td>23f2004770@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>166</td>
  <td>23f2004793@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>167</td>
  <td>23f2004936@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>168</td>
  <td>23f2004979@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>169</td>
  <td>23f2005010@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>170</td>
  <td>23f2005193@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>171</td>
  <td>23f2005325@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>172</td>
  <td>23f2005398@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>173</td>
  <td>23f2005474@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>174</td>
  <td>23f2005525@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>175</td>
  <td>23f2005665@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>176</td>
  <td>23f2005701@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>177</td>
  <td>23f2005706@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>178</td>
  <td>23f2005738@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>179</td>
  <td>23f3000975@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>180</td>
  <td>23f3001271@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>181</td>
  <td>23f3001462@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>182</td>
  <td>23f3001572@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>183</td>
  <td>23f3001745@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>184</td>
  <td>23f3001752@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>185</td>
  <td>23f3001764@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>186</td>
  <td>23f3001848@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>187</td>
  <td>23f3002196@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>188</td>
  <td>23f3002427@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>189</td>
  <td>23f3002537@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>190</td>
  <td>23f3002643@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>191</td>
  <td>23f3003016@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>192</td>
  <td>23f3003027@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>193</td>
  <td>23f3003871@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>194</td>
  <td>23f3004013@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>195</td>
  <td>23f3004024@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>196</td>
  <td>23f3004066@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>197</td>
  <td>23f3004134@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>198</td>
  <td>23f3004230@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>199</td>
  <td>23f3004238@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>200</td>
  <td>23f3004264@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>201</td>
  <td>23f3004394@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>202</td>
  <td>23f3004444@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>203</td>
  <td>24ds1000079@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>204</td>
  <td>24ds2000062@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>205</td>
  <td>24ds2000101@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>206</td>
  <td>24ds2000112@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>207</td>
  <td>24ds3000028@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>208</td>
  <td>24ds3000031@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>209</td>
  <td>24ds3000074@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>210</td>
  <td>24f1000010@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>211</td>
  <td>24f1000400@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>212</td>
  <td>24f1000784@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>213</td>
  <td>24f1000925@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>214</td>
  <td>24f1001396@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>215</td>
  <td>24f1001439@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>216</td>
  <td>24f1001520@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>217</td>
  <td>24f1002390@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>218</td>
  <td>24f1002474@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>219</td>
  <td>24f2000994@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>220</td>
  <td>24f2002746@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>221</td>
  <td>24f2003375@ds.study.iitm.ac.in</td>
  </tr>
  <tr>
  <td>222</td>
  <td>24f2004863@ds.study.iitm.ac.in</td>
  </tr>
  </tbody>
  </table>
  </div><p>Kind regards,<br>
  TDS Team</p>
  
  # topic_id
  
  168011
  
  # topic_title
  
  Q3, GA5 not accepting right answer

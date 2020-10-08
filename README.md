# Slow-Loris-Attack
<p>
 <b>SlowHTTPTest</b> is a highly configurable tool that simulates some Application Layer Denial of Service attacks by prolonging HTTP connections in different ways. 
<br>
It can be used to test your web servers for DoS vulnerabilities, or just to figure out how many concurrent connections it can handle.
</p>
<h4>Advantages</h4>
<ul>
 <li>Helps to test against DoS vulnerabilities.</li>
 <li>Helps to test the number of clients a server will be able to handle concurrently.</li>
</ul>
<h4>Disadvantages</h4>
<ul>
 <li>Hackers may use it to bring down a server, thus bringing down that server’s services.</li>
</ul>
<h4>Understanding the Technique</h4>
<img src="https://www.researchgate.net/profile/Sharmistha_Dey/publication/262843630/figure/fig4/AS:667618851708938@1536184146977/DoS-Attack-Figure-7-DDoS-Attack.ppm"/>
The technique it follows to take down a server is:
<ul>
 <li>Opening up multiple connections with the server in different intervals of time.</li>
 <li>Sending Partial/incomplete HTTP requests to the server.</li>
 <li>Thus, after a point in time, the server cannot accept anymore requests, as it gets overloaded with already sent multiple & partial requests in the pipeline.</li>
Thus, the server goes into the Denial of Service state.
</ul>
This is <b>Slowloris DOS Attack</b>.
<h4>How to migrate/prevent Slow Loris Attacks?</h4>
<ul>
 <li>Increase the maximum number of clients the Web Server will allow.</li>
 <li>Limit the number of connections a single IP address is allowed to attempt.</li>
 <li>Place restrictions on the minimum transfer speed a connection is allowed.</li>
 <li>Constrain the amount of time a client is permitted to stay connected.</li>
</ul>
<hr>
<a href="https://github.com/shekyan/slowhttptest">Here</a> is the original repository of this tool.
<h4>Original Tool Features:</h4>
<ul>
 <li>Slowing down either the header or the body section of the request.</li>
 <li>Random size of follow-up chunks, limited by optional value.</li>
 <li>Configurable interval between follow-up data chunks.</li>
 <li>Support for SSL.</li>
 <li>Support for hosts names resolved to IPv6.</li>
 <li>Verbosity levels in reporting.</li>
 <li>Connection state change tracking.</li>
 <li>Variable connection rate.</li>
 <li>Detailed statistics available in CSV format and as a chart generated as HTML file using Google Chart Tools.</li>
</ul>
<hr>
<h4>Features we have developed in this assignment</h4>
<ul>
 <li>Creation of multiple client sockets with the server.</li>
 <li>Slowing Down the server by slowing down the headers through HTTP Requests.</li>
 <li>Analyze how many concurrent sockets the server can handle.</li>
</ul>
<hr>
<h4>Testing this repository</h4>
<ul>
 <li>Start the server by typing the following command in the terminal: <pre><code>python startserver.py</code></pre></li>
 <li>Starting the Check Server script: <pre><code>python checkstatus.py</code></pre></li>
 <li>Running the Script: <pre><code>python script.py <i>address portnumber numberofsockets</i></code></pre></li>
 <b>Note:</b> In order to understand the capacity of how many sockets the server can handle, increase the numberofsockets gradually.
</ul>

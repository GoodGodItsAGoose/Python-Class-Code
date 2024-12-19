import logo from './logo.svg';
import './App.css';
import React from 'react';

function App() {
  return (
    <div className="App">
      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
      <body className="App-body">
        <div className="Body-bubble">
          <div className="Body-bubble-inner">
            <div className="Smaller-Bubble-1">
              <h1>
                CONVOLUTED MESSAGE ENCRYPTOR
              </h1>
            </div>
            {/* <video width="320" height="240" autoplay>
              <source src="https://www.youtube.com/watch?v=Lsq0FiXjGHg" type="video/mp4"></source>
              <source src="https://www.youtube.com/watch?v=Lsq0FiXjGHg" type="video/ogg"></source>
              Your borwser does not support the video tag.
            </video> */}
            <div class="Text-div">
              <p class="Top-p">The Convoluted Message Encrypter is a program used to encode messages using a six digit number that is then encrypted using a password that is entered. To decode the message, you need the message, the encoded number, and the password to decode the encoded number. </p>
              <p>This program can be used to send secret messages to one another, encode passwords so that it is annoying to figure out what password it is, or to send very serious confidential federal messages and information to teens using something like whatsapp. The program currently is not in an app format, so you will have to download the program and run it on your own.</p>
              <p>To use this program, you enter a message into the message area, then a password into the password area. The message will be encrypted by a randomized six digit code (ex: 610892), then that code will be encrypted using the password you've inputted. The output will appear below in the spaces available, you must save all the info on your own, as if you reload the page, your message, encoded code, and password will not be saved.</p>
              <p>The creators of the Convoluted Message Encryptor are not responsible for any chaos, legal troubles, drama, consequences, issues that arise that may occur. Please use wisely and safely.</p>
              <div class="message-div">
                <form action="encoding.js">
                  <label for="message" id="message-label">Message:<textarea id="message" name="message" rows="5" cols="50" placeholder="Type message here"></textarea></label>
                  <label for="password" id="password-label">Password:<input id="password" name="password" placeholder="Type password here"></input></label>
                  <label for="choice-encrypt" id="encrypt-label"><input type="radio" class="inline" id="choice-encrypt" value="choice-encrypt" onclick="Check()" />Encrypt message</label>
                  <label for="choice-encrypt" id="decrypt-label"><input type="radio" class="inline" id="choice-decrypt" value="choice-decrypt" onclick="Check()" />Decrypt message</label>
                  <div class="break"></div>
                  <input id="encrypt" type="submit" value="Encrypt!" style={{display:"block"}} />
                  <input id="decrypt" type="submit" value="Decrypt!" style={{display:"none"}} />
                  <div class="break"></div>
                </form>
                <div class="outer-outcome-div">
                  <p class="outcome-label-p">Encrypted Message:</p>
                  <div class="outcome-div" id="outcome-message-div">
                    <p class="outcome-p">Encrypted message will appear here.</p>
                  </div>
                  <p class="outcome-label-p">Encrypted Code:</p>
                  <div class="outcome-div">
                    <p class="outcome-p">Encoded code will appear here.</p>
                  </div>
                  <p class="outcome-label-p">Password Used:</p>
                  <div class="outcome-div">
                    <p class="outcome-p">Password will appear here.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
      </body>
    </div>
  );
}

function Check() {
  const x = document.getElementById("choice").getValue
  const button1 = document.getElementById("encrpyt")
  const button2 = document.getElementById("decrypt")
  if (x="encrypt") {
    button1.display = "block"
    button2.display = "none"
  };
  if (x="decrypt") {
    button1.display = "none"
    button2.display = "block"
  };
}


export default App;

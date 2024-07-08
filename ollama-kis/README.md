<div align="center">
  <img alt="ollama" height="200px" src="first-time-install/ollama-kis-logo.jpg">
</div>

<h1>Installation - Open WebUI for Drivers Education</h1> 

 <table>
  <tr>
    <th>Step</th>
    <th>Screenshot</th>
    <th>Description</th>
  </tr>   
      <tr>
    <td>Install Python for Windows  <br><br></td>
    <td><img alt="ollama" src="first-time-install/install-python.jpg"></td>
    <td> <a href="https://www.python.org/downloads/" target="new">Download Python for Windows</a> and follow instructions for installation. </td>
  </tr>
   <tr>
    <td>Install Ollama for Windows  <br><br></td>
    <td><img alt="ollama" src="first-time-install/ollama-download.jpg"></td>
    <td> <a href="https://ollama.com" target="new">Download Ollama for Windows</a> and follow instructions for installation.  <br><br></td>
  </tr>
      <tr>
    <td>Install Docker Desktop for Windows  <br><br></td>
    <td><img alt="ollama" src="first-time-install/docker-download2.jpg"><br><img alt="ollama" src="first-time-install/docker-download3.jpg"></td>
    <td> <a href="https://www.docker.com/products/docker-desktop/" target="new">Download Docker Desktop for Windows</a> and follow instructions for installation. <br><br> Recommend, going into settings and select General > Start Docker Desktop when you sign in to your computer.   <br><br><a href="first-time-install/Docker Installation Issue.txt">How to correct the Docker Installation Issue for Lenovo</a> </td>
  </tr> 
       <tr>
    <td>Pull LLM for Ollama<br><br></td> 
    <td><img alt="ollama" src="first-time-install/pull-model.png"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
    ollama pull llama3
    </td>
  </tr>  
  <tr>
    <td>Install <a href="https://docs.openwebui.com" target="new">Open WebUI</a><br><br></td>
    <td><img alt="openwebui" src="first-time-install/install-open-webui.jpg"><br><img alt="openwebuidocker" src="first-time-install/docker-install-open-webui.jpg"></td> 
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
      docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
    </td>
  </tr>  
        <tr>
    <td>Run Open-WebUI from Docker<br><br></td>
    <td><img alt="openwebui" src="first-time-install/run-open-webui-docker.png"></td> 
    <td>
     Select the 3000:8080 link to view the Open WebUI interface   
    </td>
  </tr>
     <tr>
    <td>Run Open WebUI in browser <br><br></td>
    <td><img alt="openwebuidocker" src="first-time-install/open-webui-drivers-ed-model-page.png"><br><img alt="openwebuidocker" src="first-time-install/open-webui-drivers-ed-model3c.png"><br><img alt="openwebui" src="first-time-install/open-webui-drivers-ed-model3.png"><br><img alt="openwebui" src="first-time-install/open-webui-drivers-ed-model3b.png"><br></td> 
    <td>
      <OL>
         <LI>Visit https://openwebui.com/m/sodkgb/drivers_education:latest
         <LI> Select Get 
        <li> Enter: http://localhost:3000
          <LI> Select Save & Create
        <LI> You can now select the Drivers Education Model from the drop down menu
      </ol>      
    </td>
  </tr>  
        <tr>
    <td colspan="3"><div align=center><b>Congratulations you can now run the custom Drivers Education Model!</b></div>    
    </td>
  </tr>  
</table> 



<h1>Local Install of Custom GUI </h1>
<table>
  <tr>
    <th>Step</th>
    <th>Screenshot</th>
    <th>Description</th>
  </tr>   
        <tr>
    <td>Install Python for Windows  <br><br></td>
    <td><img alt="ollama" src="first-time-install/install-python.jpg"></td>
    <td> <a href="https://www.python.org/downloads/" target="new">Download Python for Windows</a> and follow instructions for installation. </td>
  </tr>
   <tr>
    <td>Install Ollama for Windows  <br><br></td>
    <td><img alt="ollama" src="first-time-install/ollama-download.jpg"></td>
    <td> <a href="https://ollama.com" target="new">Download Ollama for Windows</a> and follow instructions for installation.  <br><br></td>
  </tr>
    <tr>
    <td>Pull LLM for Ollama<br><br></td> 
    <td><img alt="ollama" src="first-time-install/pull-model.png"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
    ollama pull llama3
    </td>
  </tr>  
  </tr>
  <tr>
    <td>Create local directory for this example <br><br></td>
    <td><img alt="ollama" src="first-time-install/make_ai_directory.jpg"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
    cd\<br>
    mkdir ai<br>
    cd\ai<br>
    You should see this c:\ai      
    </td>
  </tr>  
   <tr>
    <td>Clone github package (While in the c:\ai directory) first timers may need to install - https://gitforwindows.org/ (restart of pc recommended) <br><br>
</td>
    <td><img alt="ollama" src="first-time-install/git-clone.png"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
     git clone https://github.com/elearningshow/ollama-kis.git <br><br>
This will download all the required files to your pc. <br><br></td>
  </tr>
    <tr>
    <td>Copy/Move Test Project <br><br></td>
    <td><img alt="ollama" src="first-time-install/sample-project-directory.jpg"></td>
    <td>To ease setup copy the contents of kis-drivers-ed to c:\ai\kis-drivers-ed <br><br></td>
  </tr>  
   <tr>
    <td>Activate python environment <br><br></td>
    <td><img alt="ollama" src="first-time-install/python-activate.jpg"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
    .venv\Scripts\activate.bat  <br><br></td>
  </tr>  
  <tr>
    <td>Install requirements  <br><br></td>
    <td><img alt="ollama" src="first-time-install/pip-requirements.jpg"></td>
    <td>In windows, type <b>cmd</b> in the start menu to bring up command window.  Then type the following:<br><br>
    python.exe -m pip install --upgrade pip <br><br>
    pip install -r requirements.txt</td>
  </tr>  
     <tr>
    <td>Configure  <br><br></td>
    <td><img alt="ollama" src="first-time-install/configure_vars1.jpg"><BR><img alt="ollama" src="first-time-install/configure_vars2.jpg"></td>
    <td>You can use a basic text editor such as <a href="https://notepad-plus-plus.org/downloads/" target="new">Notepad++</a>, open the file named app.py and revise the content to make your own unique LLM.  <br><br> This LLM will be limited to the content found within the cloned base model and any additional RAG files used with the selected model.</td>
  </tr>  
   <tr>
    <td>Run - Custom LLM Model (This file will open your default browser, start a local server) <br><br></td>
    <td><img alt="ollama" src="first-time-install/startserver-ask.jpg"></td>
    <td>In windows, browse to view the content in the AI folder.  Then select the following:<br><br>
    startserver-ask.bat <br><br></td>
  </tr>  
          <tr>
    <td colspan="3"><div align=center><b>Congratulations you can now run the custom Drivers Education Model with a basic user interface. </b></div>    
    </td>
  </tr>  
</table> 






# Speech-Recognition-and-Response

## Summary
This project serves as a template for a simple speech recognition and response program. The speech recognition package is a wrapper for PyAudio and GoogleRecognize to translate speech to text. The package pyttsx3 serves to echo back commands and interface with the device. Plotly is used to visualize how these commands impact a 2-Dimensional scatter plot. Modifications to the vizualization were made to be compatible with Spyder. 

Actual workflow of the project is as follows, a scatterpoint is created at the origin and a list of key words (commands) are instantiated as well as some confirmation commands and the recognizer (converts audio input to text). From this point the application activates the microphone and prints the notification "Mic Hot." After receiving the command it will print the notification "Mic Closed." The program will then repeat the command back to the user for verbal confirmation, which upon being confirmed it will complete the command. If the command is rejected or if the command is unintelligible separate fail instances can be occur for error handling. 

## Potential Modifications/Improvements
Depending on the use-case, it can be an improvement to capture the initial audio through a trigger or an "always listening" mode. The former allows the machine to process the information intended to be sent faster, while the second may enable quicker operator response. To tailor the algorithm to your specific project, you can simply replace the series of if conditions and the key words as desired.

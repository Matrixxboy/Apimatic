# API Documentation

## Flask API Endpoints

### `GET /`
- **Endpoint:** `GET /`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - The endpoint serves as the main entry point for the AI Chat Backend API, providing a summary of available endpoints. When a GET request is made to this endpoint, it returns a JSON object containing a message and a list of other API endpoints with their respective HTTP methods. There is no middleware involved, and the response is directly generated and returned as a JSON object.
- **Handlers:**
  - Handler 1:
```python
def index():
    return jsonify({
        'message': 'AI Chat Backend API with Gemini',
        'endpoints': {
            '/api/chat': 'POST - Send chat message',
            '/health': 'GET - Health check',
            '/static/audio/<filename>': 'GET - Serve audio files'
        }
    })
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_

### `POST /api/chat`
- **Endpoint:** `POST /api/chat`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - The endpoint processes a chat request by receiving JSON data containing user input text and conversation history. It first checks if the 'text' field is provided; if not, it returns a 400 error. If valid, it generates a response using the 'get_gemini_response' function, converts the response to speech using gTTS, and saves the audio file. Finally, it constructs a URL for the audio file and returns both the AI response text and the audio URL in a JSON format. If any exceptions occur during processing, a 500 error is returned.
- **Handlers:**
  - Handler 1:
```python
def chat():
    try:
        data = request.get_json()
        user_text = data.get('text', '')
        conversation_history = data.get('conversationHistory', [])

        if not user_text:
            return jsonify({'error': 'No text provided'}), 400

        ai_response = get_gemini_response(user_text, conversation_history)
        
        tts = gTTS(text=ai_response, lang='en', slow=False)
        
        timestamp = int(time.time() * 1000)
        filename = f"response_{timestamp}.mp3"
        filepath = os.path.join(STATIC_DIR, filename)
        
        tts.save(filepath)
        
        audio_url = f"http://localhost:5000/static/audio/{filename}"
        
        return jsonify({
            'responseText': ai_response,
            'audioUrl': audio_url
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({'error': 'Internal server error'}), 500
```
- **Query Params:**
  _None_
- **Request Body:**
  Contains the user's input text and conversation history for generating a response.
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string",
      "description": "The text input from the user for which a response is to be generated."
    },
    "conversationHistory": {
      "type": "array",
      "description": "An array of previous messages in the conversation to provide context."
    }
  },
  "required": [
    "text"
  ]
}
```

### `GET /health`
- **Endpoint:** `GET /health`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - The endpoint checks the health status of the AI Chat Backend service. It evaluates the 'model' variable to determine if the service is operational. If 'model' is truthy, it sets 'gemini_status' to 'ok'; otherwise, it sets it to 'error'. The endpoint then returns a JSON response containing a general health status, a message indicating that the backend is running, and the specific status of the 'gemini' component.
- **Handlers:**
  - Handler 1:
```python
def health():
    gemini_status = "ok" if model else "error"
    return jsonify({
        'status': 'healthy', 
        'message': 'AI Chat Backend is running',
        'gemini_status': gemini_status
    })
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_

### `GET /static/audio/<filename>`
- **Endpoint:** `GET /static/audio/<filename>`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - The endpoint serves audio files from a specified static directory. It takes a 'filename' parameter, which is used to locate the audio file within the STATIC_DIR. The function uses 'send_from_directory' to securely send the requested file to the client. If the file does not exist, a 404 error will be returned automatically by the framework.
- **Handlers:**
  - Handler 1:
```python
def serve_audio(filename):
    return send_from_directory(STATIC_DIR, filename)
```
- **Query Params:**
  _None_
- **Request Body:**
  _None_

# API Documentation

## Flask API Endpoints

### `GET /`
- **Endpoint:** `GET /`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - This endpoint acts as an index or landing page for the API, providing a list of available endpoints and their corresponding HTTP methods.  It doesn't involve any database interaction or complex logic; it simply returns a hardcoded JSON response containing a welcome message and a dictionary of API routes and their descriptions. There is no middleware involved in this particular endpoint.
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
  This endpoint does not accept a request body.

### `POST /api/chat`
- **Endpoint:** `POST /api/chat`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - This endpoint handles text-based chat requests. It receives user input and conversation history via a JSON payload.  The endpoint first checks if user input text is provided; if not, it returns a 400 Bad Request error. If text is present, it uses a function `get_gemini_response` (not shown in the provided code) to generate an AI response.  The response is then converted to speech using gTTS, saved as an MP3 file in the application's static directory, and its URL is included in the JSON response.  Error handling is implemented using a try-except block to catch and log any exceptions, returning a 500 Internal Server Error response in case of failure. The endpoint returns a JSON object containing the AI's text response and a URL to access the corresponding audio file.
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
  The endpoint expects a JSON payload containing the user's text input and optional conversation history.
```json
{
  "type": "object",
  "properties": {
    "text": {
      "type": "string",
      "description": "The user's text input.  Required."
    },
    "conversationHistory": {
      "type": "array",
      "description": "An array of previous messages in the conversation. Optional."
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
  - This endpoint is designed to check the health status of the AI Chat Backend.  It directly returns a JSON response indicating whether the backend is running ('healthy') and includes a 'gemini_status' field reflecting the operational status of the Gemini model. If the 'model' variable (presumably representing the Gemini model's availability) is true, 'gemini_status' is set to 'ok'; otherwise, it's set to 'error'. No external services or databases are accessed; the response is constructed entirely from internal variables.
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
  This endpoint does not require a request body.

### `GET /static/audio/<filename>`
- **Endpoint:** `GET /static/audio/<filename>`
- **Source File:** `flaskDemo.py`
- **Logic Explanation:**
  - This endpoint serves audio files.  It receives a filename as input, uses the `send_from_directory` function to locate the file within the directory specified by the `STATIC_DIR` variable, and returns the file's contents as the response.  No middleware is explicitly shown in this code snippet. Error handling (e.g., for file not found) is not explicitly defined in this function but would likely be handled by the `send_from_directory` function or a higher-level framework.
- **Handlers:**
  - Handler 1:
```python
def serve_audio(filename):
    return send_from_directory(STATIC_DIR, filename)
```
- **Query Params:**
  _None_
- **Request Body:**
  None.  The filename is provided as a path parameter, not in the request body.

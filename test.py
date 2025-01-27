from flask import Flask, request, jsonify
import openai
from flask_cors import CORS  # Import CORS

# Set up the Flask app
app = Flask(__name__)

# Enable CORS for all domains
CORS(app)
# OpenAI API key
openai.api_key = "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"

@app.route("/generate", methods=["POST"])
def generate_message():
    try:
        # Get the prompt from the request
        data = request.json
        prompt = data.get("prompt", "")

        if not prompt:
            raise ValueError("Prompt is required")

        # Call the OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
        )
        
        # Extract the generated message
        message = response["choices"][0]["message"]["content"].strip()
        return jsonify({"message": message})  # Return the result as JSON

    except openai.error.OpenAIError as e:
        # Catch OpenAI-specific errors
        return jsonify({"error": f"OpenAI error: {str(e)}"}), 500
    except Exception as e:
        # Catch any other errors
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)


#    const apiKey = "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";

import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from openai import OpenAI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    try:
        # Get API key from environment variable
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return HTMLResponse("""
            <html>
            <body>
            <h1>Welcome to AI Voyage!</h1>
            <p>OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.</p>
            </body>
            </html>
            """)
        
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Give a cheerful welcome message to the user"},
            ]
        )
        reply = response.choices[0].message.content
        html_content = f"""
        <html>
        <body>
        <h1>{reply}</h1>
        </body>
        </html>
        """
        return html_content
    except Exception as e:
        # Return a friendly error page instead of crashing
        return HTMLResponse(f"""
        <html>
        <body>
        <h1>Welcome to AI Voyage!</h1>
        <p>Sorry, we're experiencing some technical difficulties. Please try again later.</p>
        <p>Error: {str(e)}</p>
        </body>
        </html>
        """, status_code=200)  # Return 200 to avoid 500 errors